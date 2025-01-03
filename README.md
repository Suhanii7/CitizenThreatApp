# Citizen Threat Reporting App

A simple and intuitive application for citizens to report and view threats in their community. The app uses Firebase for storing and retrieving reports, ensuring seamless data management and scalability.

---

## 📋 Purpose

The **Citizen Threat Reporting App** empowers users to:
- Report threats by providing a description, location, and time.
- View all submitted reports in a sorted and organized manner based on submission time.
- Enhance community safety by providing a centralized platform for threat reporting and awareness.

---

## 🛠️ Technologies Used

### 1. **Kivy**
   - **Why**: Kivy is a Python-based framework that enables the development of cross-platform applications with a modern and responsive UI.
   - **Usage**: Used to design and implement the application's user interface and handle interactions like form submission and navigation.

### 2. **Firebase (Firestore)**
   - **Why**: Firebase provides a scalable and real-time database solution with easy integration and high availability.
   - **Usage**: Used for storing and retrieving threat reports, ensuring data persistence and security.

### 3. **Python**
   - **Why**: Python is a versatile and developer-friendly language, making it ideal for rapid prototyping and app development.
   - **Usage**: The backbone of the app, handling UI logic, Firebase integration, and report management.

---

## 🖥️ Features

1. **Report Threat**
   - Users can submit a threat report with the following details:
     - Description of the threat.
     - Location of the threat.
     - Automatic timestamp of the submission.
   - Data is stored securely in Firestore.

2. **View Reports**
   - Users can view all submitted reports.
   - Reports are displayed with:
     - Description
     - Location
     - Submission time
   - Reports are sorted in reverse chronological order for better usability.

3. **Responsive UI**
   - A clean and user-friendly interface designed with Kivy for an intuitive user experience.

---

## 📖 Why This Project?

- **Community Impact**: Provides a centralized platform for threat reporting, encouraging active participation in community safety.
- **Scalability**: By leveraging Firebase, the app is designed to handle increasing data volumes without performance degradation.
- **Learning Opportunity**: Demonstrates the integration of Kivy for UI and Firebase for backend, serving as a learning tool for app development enthusiasts.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Firebase account with a Firestore database
- Firebase service account key file

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Suhanii7/CitizenThreatApp.git
   cd CitizenThreatApp
