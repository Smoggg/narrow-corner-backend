import os
import uvicorn

from dotenv import load_dotenv

load_dotenv()

PORT = int(os.environ.get("PORT", 8080))


if __name__ == "__main__":
    uvicorn.run("src.api:app", host="0.0.0.0", port=PORT, reload=True)
