# Face Recognition + Attendance System

This project is a Python-based application for real-time face recognition and attendance tracking. It uses **OpenCV** and **face_recognition** libraries for detecting and recognizing faces, and records attendance data in a structured format.

---

## Features

- **Face Recognition**: Detects and recognizes faces in real-time using pre-trained models.
- **Attendance Tracking**: Automatically logs the attendance of recognized individuals.
- **Database Integration**: Stores attendance records for easy retrieval and analysis.
- **Scalability**: Can add new faces to the dataset dynamically.

---

## Prerequisites

1. Python 3.8+
2. Libraries:
   - OpenCV
   - face_recognition
   - NumPy
   - pandas

Install the required libraries:
```bash
pip install opencv-python face_recognition numpy pandas
```

3. A webcam or a video input source.

---

## How It Works

1. **Face Encoding**:
   - Load known images and compute face encodings.
   - Save these encodings in a file or database.

2. **Real-Time Recognition**:
   - Use the webcam feed to detect faces.
   - Compare detected faces with the known encodings.

3. **Attendance Logging**:
   - If a face is recognized, log the name and timestamp in an attendance file.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/username/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. Add images of known individuals to the `ImagesBasic` folder. Name the images with the individual's name, e.g., `John_Doe.jpg`.

3. Run the `Basics.py` script to encode faces:
   ```bash
   python Basics.py
   ```

4. Start the face recognition and attendance system:
   ```bash
   python AttendenceProject.py
   ```

---

## Files and Directories

- `AttendenceProject.py`: Main script for real-time face recognition and attendance.
- `Basics.py`: Script to encode known faces.
- `ImagesBasic/`: Directory containing images of known individuals.
- `Attendence.csv`: File where attendance records are stored.

---

## Output

The application generates an `Attendence.csv` file with the following columns:

| Name         | Date       | Time       |
|--------------|------------|------------|
| John Doe     | 2024-12-25 | 10:00:00   |
| Jane Smith   | 2024-12-25 | 10:15:30   |

---

## Demo

Here is an example of the application in action:

1. **Face Detection**:
   Real-time detection of faces in the video feed.

2. **Attendance Logging**:
   Automatic logging of recognized faces with a timestamp.

---

## Future Enhancements

- **Integration with Databases**: Store attendance records in a SQL or NoSQL database.
- **GUI**: Add a graphical user interface for easier interaction.
- **Multi-Camera Support**: Enable support for multiple video sources.

