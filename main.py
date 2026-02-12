import cv2
import face_recognition
import numpy as np
import os

USERS_FOLDER = "users"  # Folder where all face data will be stored

# Create folder if it doesn't exist (Database setup)
if not os.path.exists(USERS_FOLDER):
    os.makedirs(USERS_FOLDER)

def register_user():
    cap = cv2.VideoCapture(0)
    # Request name from user
    name = input("👤 Enter the name of the person to register: ").strip()
    
    if name == "":
        print("❌ Name cannot be empty!")
        return

    print(f"📸 REGISTRATION MODE for '{name}': Look at the camera and press 's'!")
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        cv2.putText(frame, "Press 's' to Save", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("REGISTRATION SCREEN", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb)
            
            if len(faces) > 0:
                # Encode the face
                enc = face_recognition.face_encodings(rgb, faces)[0]
                
                # Save file with name: users/john.npy
                file_path = os.path.join(USERS_FOLDER, f"{name}.npy")
                np.save(file_path, enc)
                
                print(f"✅ SUCCESS: {name} added to database!")
                break
            else:
                print("❌ Face not found! Try again.")
                
    cap.release()
    cv2.destroyAllWindows()

def load_database():
    """Loads all .npy files from the folder into memory."""
    known_faces = []
    known_names = []
    
    # Iterate through files in the folder
    files = os.listdir(USERS_FOLDER)
    
    if len(files) == 0:
        return [], []

    print("📂 Loading database...")
    for file in files:
        if file.endswith(".npy"):
            
            # Extract name from filename (john.npy -> john)
            name = os.path.splitext(file)[0]
            
            # Load the data
            encoding = np.load(os.path.join(USERS_FOLDER, file))
            
            known_faces.append(encoding)
            known_names.append(name)
            
    print(f"✅ {len(known_names)} people loaded into memory.")
    return known_faces, known_names

def start_system():
    # 1. Load all registered people first
    known_faces, known_names = load_database()
    
    if not known_faces:
        print("⚠️ Database is empty! You must register first.")
        return

    print("🔐 SYSTEM ACTIVE (Press 'q' to Exit)")
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Resize for performance
        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
        
        locs = face_recognition.face_locations(rgb)
        encs = face_recognition.face_encodings(rgb, locs)
        
        for (top, right, bottom, left), face_encoding in zip(locs, encs):
            
            # --- MULTI-USER LOGIC ---
            # 1. Measure distance (difference) to all known faces
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            
            # 2. Find the lowest difference (closest match)
            best_match_index = np.argmin(face_distances)
            best_match_distance = face_distances[best_match_index]
            
            # 3. If difference is less than 0.6 it is a MATCH, otherwise UNKNOWN
            if best_match_distance < 0.6:
                name = known_names[best_match_index].upper()
                color = (0, 255, 0) # Green
            else:
                name = "UNKNOWN"
                color = (0, 0, 255) # Red
            
            # Correct coordinates and draw
            top *= 4; right *= 4; bottom *= 4; left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, f"{name} ({int((1-best_match_distance)*100)}%)", (left + 6, bottom - 6), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

        cv2.imshow("SECURITY CAMERA", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        choice = input("\n--- MENU ---\n1: Register New Person\n2: Start System\n3: Exit\nYour Choice: ")
        if choice == '1': register_user()
        elif choice == '2': start_system()
        elif choice == '3': break
        else: print("Invalid choice.")