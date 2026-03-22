# 📰 News Fetcher CLI (Python)

A simple and efficient command-line application that fetches the latest news articles based on user input using the **NewsAPI**.

---

## 🚀 Features

- 🔍 Search news by topic (technology, sports, business, etc.)
- 📰 Fetch real-time articles
- 📊 Sorted by popularity
- 🔗 Direct article links
- ⚡ Fast and lightweight CLI tool

---

## 🛠️ Tech Stack

- Python 3
- Requests Library
- NewsAPI

---

## 📦 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/CodeWithShrey-collab/News-Fetcher-CLI.git
cd news-fetcher-python
```

---

2. Install dependencies:
```bash
pip install requests
```

---

🔑 API Setup
Go to: https://newsapi.org/
Sign up and get your API key
Replace the API key in the code:
```bash
api = "YOUR_API_KEY"
```

---

▶️ Usage

Run the script:
```bash
python main.py
```

---

Enter your desired news topic:
```bash
What type of news are you interested in today? technology
```

---

📌 Example Output
```bash
1. Apple launches new AI feature https://example.com/article1

*****************************************

2. AI is transforming the future https://example.com/article2
```

---

📁 Project Structure
```bash
news-fetcher-python/
│
├── main.py
└── README.md
```

---

⚠️ Notes
- Free NewsAPI plan has request limits.
- Date is currently fixed in code (2026-03-21) — can be improved dynamically.
---

💡 Future Improvements
- 📅 Dynamic date selection
- 🌐 GUI version (Tkinter / Web app)
- 🗂️ Category-based filtering
- 💾 Save articles to file (PDF/CSV)
- 🔔 Notifications for trending news
---

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.
---

📜 License

This project is licensed under the MIT License.
---

🙌 Acknowledgements
NewsAPI
Python Requests Library
