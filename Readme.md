# 🎉 Event Management System

A professional and robust **Event Management System** designed to simplify managing members, events, registrations, and admin-level reporting through a clean console interface backed by a FastAPI server.

This system ensures secure data handling, clear modular architecture, and persistent **text-based file storage** — designed for academic and production-style environments.

---

## 🚀 Features

-   👤 **Member Management (Full CRUD)**
    -   Create new members with unique IDs.
    -   Read/List all members.
    -   Update member details.
    -   Delete members securely (prevents deletion if active bookings exist).

-   🗓️ **Event Creation & Management (Full CRUD)**
    -   Create events with strict validation (Fee ≥ 0, Capacity > 0).
    -   Read/List available events.
    -   Update event details.
    -   Delete cancelled events.

-   📝 **Smart Registration System**
    -   Transaction-safe booking process.
    -   Auto-checks event capacity to prevent overbooking.
    -   Prevents duplicate registrations.
    -   Auto-generates unique Registration IDs.

-   🔐 **Admin Panel**
    -   Secure Login Authentication.
    -   💰 **Revenue Report:** Calculates total earnings per event.
    -   📜 **Audit Log:** Tracks all system activities (Add/Update/Delete actions).

-   💾 **Persistent Text File Storage**
    -   Uses `.txt` files (`events.txt`, `members.txt`, etc.) for lightweight and portable data persistence.

-   ⚙️ **Architecture**
    -   **Client:** Console-based frontend using Python `requests`.
    -   **Server:** High-performance Backend API using `FastAPI` and `Uvicorn`.

---

## 🛠️ Technologies Used

-   **Python 3.12+**
-   **Backend Framework:** FastAPI
-   **Server:** Uvicorn (ASGI Server)
-   **HTTP Client:** Python Requests
-   **Data Validation:** Pydantic
-   **Storage:** Text File Database (.txt)
-   **Version Control:** Git & GitHub

---

# 📂 Project Structure

```bash
EventManagementSystem/
│
├── main.py                         # 🚀 Server Entry Point (Runs Uvicorn)
│
├── server/                         # 🧠 Backend Logic + API
│   ├── storage.py                  # Handles Read/Write operations for .txt files
│   ├── app.py                      # API Router Configuration
│   ├── api_member_management.py    # Member CRUD API
│   ├── api_event_management.py     # Event CRUD API
│   ├── api_registration_system.py  # Registration Logic API
│   └── api_report_admin_system.py  # Admin & Reporting API
│
├── client/                         # 💻 Console Client
│   ├── console.py                  # Main Menu Interface
│   ├── member_management.py        # Member Menu Logic
│   ├── event_management.py         # Event Menu Logic
│   ├── registration_system.py      # Registration Menu Logic
│   └── report_admin_system.py      # Admin Panel Logic
│
└── data/                           # 💾 Auto-Generated Data Storage
    ├── members.txt
    ├── events.txt
    ├── registrations.txt
    ├── admin.txt
    └── audit.txt

------------------------------------------------------------------------

# ⚙️ Installation Guide

Below are complete installation steps for **Windows**, **macOS**, and
**Linux**.

------------------------------------------------------------------------

# 🪟 Windows Installation

### 1️⃣ Install Git

Download: https://git-scm.com/download/win

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/SayedAliff/Event-Mangement-System
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# 🍎 macOS Installation

### 1️⃣ Install Git

``` bash
brew install git
```

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/SayedAliff/Event-Mangement-System
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip3 install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# 🐧 Linux Installation

### 1️⃣ Install Git

Ubuntu / Debian:

``` bash
sudo apt update
sudo apt install git -y
```

Fedora:

``` bash
sudo dnf install git -y
```

### 2️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/event-management-system.git
cd event-management-system
```

### 3️⃣ Install Dependencies

``` bash
pip3 install fastapi "uvicorn[standard]" requests pydantic
```

------------------------------------------------------------------------

# ▶️ Running the System

## 1️⃣ Start the Server

Windows:

``` bash
python main.py
```

macOS / Linux:

``` bash
python3 main.py
```

------------------------------------------------------------------------

## 2️⃣ Start the Console Client

Windows:

``` bash
python client/client.py
```

macOS / Linux:

``` bash
python3 client/client.py
```

------------------------------------------------------------------------

# 🎮 User Guide

### 👤 Member Management

- Add Member
- List Members
- Update Member
- Delete Members

### 🗓️ Event Management

- Create Event (fee + capacity)
- Update Event
- Prevent duplicate event IDs
- Delete Event

### 📝 Registration

- Register Member
- Auto-check capacity
- Prevent duplicate entry

### 🔐 Admin Panel

- Login: Username: admin | password: 123
- View Revenue
- View Audit Log

------------------------------------------------------------------------

# 🤝 Contributing

1. Fork
2. Create Branch
3. Commit
4. Push
5. Pull Request

------------------------------------------------------------------------ 