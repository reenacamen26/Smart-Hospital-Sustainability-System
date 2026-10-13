
# 🏥 Smart Hospital Sustainability System

## 📌 Project Overview

The Smart Hospital Sustainability System is a Python-based application designed to support hospital resource management through rule-based analysis and recommendations. It helps monitor water consumption, electricity usage, waste generation, potential water leaks, and future resource requirements.

## 🎯 Objectives

- Monitor water and electricity consumption.
- Classify waste and provide disposal recommendations.
- Identify possible water leaks using predefined conditions.
- Estimate future water requirements.
- Promote efficient resource utilization through actionable suggestions.

## 🛠️ Technologies Used

- Programming Language: Python
- Concepts: Functions, Conditional Statements, Loops, Exception Handling
- Application Type: Menu-Driven Console Application
- Decision Logic: Rule-Based System

## 🚀 Features

### 1. Water Management
- Accepts water usage and tank-level inputs.
- Classifies water usage as Normal or High.
- Identifies tank levels as Low or Sufficient.
- Provides water conservation and tank monitoring suggestions.

### 2. Electricity Management
- Evaluates electricity consumption.
- Considers whether the current period is peak time.
- Recommends energy-saving practices.

### 3. Waste Management
- Supports plastic, organic, and medical waste categories.
- Classifies waste and provides suitable handling recommendations.
- Identifies high waste generation based on a predefined threshold.

### 4. Leak Detection
- Evaluates water usage and sudden tank-level drops.
- Flags possible leaks using rule-based conditions.
- Provides inspection and maintenance recommendations.

### 5. Resource Planning
- Accepts previous water usage and expected growth.
- Calculates estimated future water requirements.
- Provides resource planning recommendations.

## 📂 Project Structure

```text
Smart-Hospital-Sustainability-System/
├── Smart hospital.py
└── README.md
```

## ⚙️ How to Run

### Prerequisites
- Python 3 installed
- Visual Studio Code or another Python editor

### Steps

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python "Smart hospital.py"
```

5. Select a module from the displayed menu.
6. Enter the requested values to view the report and recommendations.

## 🧪 Example

Water Management sample input:

- Water usage: 600 liters
- Tank level: 40%

Expected results:

- Usage Status: High
- Tank Status: Sufficient
- Recommendation: Reduce water usage
- Recommendation: Continue regular tank level monitoring

## ⚠️ Limitations

- The current application uses manually entered data.
- Thresholds are predefined examples and are not validated hospital operating standards.
- Leak detection uses simplified rules and does not connect to real sensors.
- Resource planning uses a basic percentage-growth calculation.
- The system does not currently use machine learning or a database.

## 🔮 Future Enhancements

- Integrate IoT sensors for real-time resource monitoring.
- Store historical consumption data in a database.
- Develop a graphical dashboard for reports and trends.
- Add alerts for unusual consumption and possible leaks.
- Explore predictive analytics using historical resource data.

## 👩‍💻 Author

Developed as a Python-based sustainability and resource management project.


## 📸 Project Screenshots

### 1. Main Menu
![Main Menu](screenshots/01-main-menu.png)

### 2. Water Management
![Water Management](screenshots/02-water-management.png)

### 3. Electricity Management
![Electricity Management](screenshots/03-electricity-management.png)

### 4. Waste Management
![Waste Management](screenshots/04-waste-management.png)

### 5. Leak Detection
![Leak Detection](screenshots/05-leak-detection.png)

### 6. Resource Planning
![Resource Planning](screenshots/06-resource-planning.png)
