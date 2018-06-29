from main import app
import os

port = os.getenv('PORT', 5000)
app.run(host='0.0.0.0', port=port)
