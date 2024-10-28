# Redis image officiel 
FROM python:3.12.1



COPY requierement.txt .
COPY app.py .

# Forcer l'installation des paquets malgré les restrictions
RUN pip3 install --break-system-packages -r requierement.txt

CMD ["python", "app.py"] 
