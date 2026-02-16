# Course Compass
Course Compass is a web application that allows users to predict their performance in future courses based on previous grades. It also provides a platform where students can leave reviews on classes with information such as curve, difficulty, and professor.

The application uses:

- JavaScript React for frontend
- Python FastAPI for backend
- REST API for communication between Python and JS

# How to run
In order to run this you are going to need to install Anaconda-Navigator and Node.js.
Once Anaconda is installed run the following commands in the terminal:

```
git clone https://github.com/Luke-Lindsey/Course-Compass
```
```
cd Course-Compass
```
```
conda env create -f environment.yml
```
```
conda activate course-compass
```
```
pip install fastapi uvicorn
```
```
cd backend
```
```

python -m uvicorn main:app --reload --port 8001
```
Once these are ran you should have FastAPI running at http://127.0.0.1:8001/docs.
Now open a new terminal for JS and run the following:

```
cd frontend
```
```
npm install
```
```
npm start
```

Once these are ran you should have React APP running at http://localhost:3000.
The application should now be functioning. To ensure this on the React APP page you should see a "predict" button that when pushed returns
>{"predicted_grade": "B+", "confidence": 0.85, "target": "Physics 1"}
which is a response from the python program running on port 8001.
