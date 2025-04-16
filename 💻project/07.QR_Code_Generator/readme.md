
## 📱 Project 07: QR Code Generator in Python

This project demonstrates how to generate a **QR code** using Python with just a few lines of code. QR codes can be used to store information like text, URLs, contact info, or any data that can be scanned using a QR reader.

---

### 🎯 Objective

To create a Python program that:

- Generates a QR code from a string or any custom data.
- Saves the QR code as an image file (PNG format).
- Uses the `qrcode` library to do this efficiently.

---

### 🔧 Features

- Simple and clean implementation using `qrcode.make()`
- Encodes any string (text, URL, etc.) into a QR code
- Saves the output as a PNG image file
- Beginner-friendly with no complex setup

---

## 📦 Requirements

- Python 3.x
- `qrcode` library

You can install the required library using pip:

```bash
pip install qrcode[pil]
```
---

### 💻 How to Run the Program

1. **Install the `qrcode` module** by running the following command in your terminal or command prompt:

    ```bash
    pip install qrcode[pil]
    ```

2. **Save the following code** in a Python file (e.g., `qr_generator.py`):

    ```python
    import qrcode

    data = 'QR code using make() function'
    img = qrcode.make(data)
    img.save('qr_code_project7.png')
    ```

3. **Run the script** using the following command:

    ```bash
    python qr.py
    ```

4. A **PNG image** named `qr_code_project7.png` will be created in the same folder where the script is located.



