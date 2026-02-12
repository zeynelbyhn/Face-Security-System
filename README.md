# 🔐 Biometric Face Security System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Face Recognition](https://img.shields.io/badge/AI-Face%20Recognition-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A **Real-Time Face Recognition System** built with Python that identifies users via webcam with high accuracy and speed.

---

## 🌟 Key Features

### 1. 👥 Multi-User Support
* Unlimited user registration.
* Dynamic database system using the `users/` directory.
* No retraining required when adding new users.
* Recognizes multiple faces simultaneously in real-time.

### 2. 🔒 Privacy-First Architecture (GDPR Friendly)
* **No Raw Images:** The system does **not** save user photos.
* **Vector Storage:** Faces are converted into **128-dimensional mathematical embeddings** and stored as `.npy` (NumPy) binary files.
* This ensures high security and fast processing.

### 3. ⚡ High Performance
* Optimized frame resizing (1/4 scale) for low-latency real-time processing.
* Uses **HOG (Histogram of Oriented Gradients)** and **Deep Learning** for state-of-the-art accuracy.
* Real-time confidence scoring for each detection.

### 4. 🎯 Smart Recognition
* Color-coded visual feedback (Green for known, Red for unknown).
* Displays match confidence percentage in real-time.
* Adjustable recognition threshold for security control.

---

## 📂 Project Structure

```text
Face-Security-System/
├── main.py              # The core application script
├── users/               # Database folder (auto-created on first run)
│   ├── john.npy         # Example: User face encoding
│   ├── sarah.npy        # Example: User face encoding
│   └── ...              # Additional registered users
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core programming language |
| **OpenCV (cv2)** | Real-time computer vision and video processing |
| **face_recognition** | Face detection and encoding (built on dlib) |
| **NumPy** | Numerical computing and array operations |

---

## 📋 Prerequisites

Before running this application, ensure you have:

- **Python 3.9 or higher** installed on your system
- A **webcam** connected to your computer
- **Administrator privileges** (for webcam access)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/zeynelbyhn/Face-Security-System.git
cd face-security-system
```

### Step 2: Install Dependencies

```bash
pip install opencv-python
pip install face-recognition
pip install numpy
```

### Step 3: Verify Installation

```bash
python -c "import cv2, face_recognition, numpy; print('✅ All libraries installed successfully!')"
```

> **⚠️ Windows Users:** The `face_recognition` library requires `dlib`, which needs **Visual Studio Build Tools** or **CMake**. 
> 
> **Quick Fix:**
> ```bash
> pip install cmake
> pip install dlib
> pip install face-recognition
> ```

---

## 🎯 Usage Guide

### Running the Application

```bash
python main.py
```

### Main Menu

Upon running, you'll see an interactive menu:

```
--- MENU ---
1: Register New Person
2: Start System
3: Exit
Your Choice:
```

---

### 1️⃣ Register New Person

**Purpose:** Add a new user to the security system.

**Steps:**
1. Select option `1`
2. Enter the person's full name when prompted
3. Look directly at the camera
4. Press `s` on your keyboard to capture the face
5. The system will:
   - Detect your face
   - Generate a 128-dimensional encoding
   - Save it as `users/[name].npy`

**Example:**
```
👤 Enter the name of the person to register: John Doe
📸 REGISTRATION MODE for 'John Doe': Look at the camera and press 's'!
✅ SUCCESS: John Doe added to database!
```

---

### 2️⃣ Start Recognition System

**Purpose:** Activate the real-time face recognition system.

**Steps:**
1. Select option `2`
2. The system loads all registered users from the database
3. Position yourself in front of the camera
4. The system will:
   - Detect and recognize your face in real-time
   - Display your name with confidence percentage
   - Show color-coded bounding boxes
5. Press `q` to exit the recognition mode

**Visual Feedback:**

| Indicator | Meaning |
|-----------|---------|
| 🟢 **Green Box** | Registered user identified |
| 🔴 **Red Box** | Unknown person detected |
| **Percentage** | Match confidence (higher is better) |

<img src="Ronaldo.png" width="500" height="auto" alt="Example">

<img src="Jon-Snow.png" width="500" height="auto" alt="Example">

**Example Console Output:**
```
📂 Loading database...
✅ 5 people loaded into memory.
🔐 SYSTEM ACTIVE (Press 'q' to Exit)
```

---

### 3️⃣ Exit

Select option `3` to safely close the application.

---

## 🧠 How It Works

### Face Registration Process

```
1. Webcam Capture → 2. Face Detection → 3. Face Encoding → 4. Save to Database
```

**Technical Details:**
1. **Capture:** OpenCV grabs video frames from webcam
2. **Detection:** HOG-based face detector locates facial regions
3. **Encoding:** Deep neural network generates 128-D face embedding
4. **Storage:** NumPy saves the embedding as a binary `.npy` file

### Face Recognition Process

```
1. Load Database → 2. Live Detection → 3. Distance Comparison → 4. Match/Reject → 5. Display Result
```

**Technical Details:**
1. **Load:** All `.npy` files are loaded into memory at startup
2. **Detect:** Real-time face detection on video stream (resized to 1/4 for performance)
3. **Compare:** Calculate Euclidean distance between detected face and all known faces
4. **Decision:** 
   - Distance < 0.6 → **MATCH** (Known user) ✅
   - Distance ≥ 0.6 → **UNKNOWN** (Unknown person) ❌
5. **Display:** Draw color-coded bounding box with name and confidence

### Recognition Algorithm

The system uses **Euclidean Distance** in 128-dimensional space:

```python
distance = ||face_encoding_A - face_encoding_B||
```

**Decision Logic:**
- `distance < 0.6` → **Authenticated** ✅
- `distance ≥ 0.6` → **Denied** ❌

**Confidence Calculation:**
```python
confidence = (1 - distance) × 100%
```

---

## ⚙️ Configuration & Customization

### Adjustable Parameters

Open `main.py` and modify these values:

```python
# Database location (Line 6)
USERS_FOLDER = "users"

# Recognition sensitivity (Line 110)
# Lower value = stricter matching
if best_match_distance < 0.6:  # Adjust 0.6 to your preference
    # Range: 0.4 (very strict) to 0.7 (lenient)

# Performance optimization (Line 93)
small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
# Range: fx=0.1 (faster) to fx=1.0 (more accurate)
```

### Performance Tuning

| Setting | Speed | Accuracy | Recommended For |
|---------|-------|----------|----------------|
| `fx=0.1, fy=0.1` | ⚡ Very Fast | ⭐ Low | Low-end hardware |
| `fx=0.25, fy=0.25` | ⚡ Fast | ⭐⭐⭐ Good | **Default - Balanced** |
| `fx=0.5, fy=0.5` | ⚡ Moderate | ⭐⭐⭐⭐ High | High-end hardware |
| `fx=1.0, fy=1.0` | 🐌 Slow | ⭐⭐⭐⭐⭐ Maximum | Maximum accuracy needed |

### Recognition Threshold Guide

| Threshold | Behavior | Use Case |
|-----------|----------|----------|
| `< 0.4` | Very strict - May reject valid users | High-security environments |
| `0.5` | Strict - Balanced security | Recommended for most cases |
| `0.6` | **Default** - Good balance | General use |
| `0.7` | Lenient - May accept lookalikes | Convenience over security |
| `> 0.8` | Very lenient - High false positive risk | Not recommended |

---

## 🎨 Visual Interface

### Registration Screen
```
┌─────────────────────────────┐
│  Press 's' to Save          │
│                             │
│    [Live Camera Feed]       │
│                             │
└─────────────────────────────┘
```

### Recognition Screen
```
┌─────────────────────────────────┐
│  SECURITY CAMERA               │
│                                 │
│  ┌──────────────┐              │
│  │ JOHN DOE     │              │
│  │ (95%)        │  ← Green Box │
│  └──────────────┘              │
│                                 │
│  ┌──────────────┐              │
│  │ UNKNOWN      │              │
│  │ (0%)         │  ← Red Box   │
│  └──────────────┘              │
└─────────────────────────────────┘
```

---

## 📝 Best Practices

### For Accurate Recognition

✅ **Do:**
- Use good lighting (front-facing light)
- Look directly at the camera
- Keep face clearly visible
- Register with neutral expression
- Use HD webcam for best results

❌ **Don't:**
- Wear sunglasses or masks during registration
- Register in dim lighting
- Move quickly during detection
- Use extreme angles

### For System Security

🔒 **Recommendations:**
- Keep `users/` folder secure
- Regularly backup `.npy` files
- Use strong naming conventions
- Implement encryption for production use
- Add authentication for sensitive applications

---


