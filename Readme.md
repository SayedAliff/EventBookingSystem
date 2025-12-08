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