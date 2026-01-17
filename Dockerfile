# 1. Base image – מערכת עם Python
FROM python:3.10-slim

# --- NETFREE CERT INTSALL ---
ADD https://netfree.link/dl/unix-ca.sh /home/netfree-unix-ca.sh 
RUN cat  /home/netfree-unix-ca.sh | sh
ENV NODE_EXTRA_CA_CERTS=/etc/ca-bundle.crt
ENV REQUESTS_CA_BUNDLE=/etc/ca-bundle.crt
ENV SSL_CERT_FILE=/etc/ca-bundle.crt
# --- END NETFREE CERT INTSALL ---
    
# 2. עבודה מתוך תיקייה בתוך הקונטיינר
WORKDIR /app

# 3. העתקת קובץ התלויות
COPY app/requirements.txt .

# 4. התקנת התלויות
RUN pip install --no-cache-dir -r app/requirements.txt

# 5. העתקת קוד האפליקציה
COPY app/ .

# 6. פתיחת פורט
EXPOSE 5000

# 7. הרצת האפליקציה
CMD ["python", "main.py"]
