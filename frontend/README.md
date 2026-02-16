<<<<<<< HEAD
=======
<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
>>>>>>> 8bd4555d53a8a63815a66c30803b3a0eeb24591d
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
<<<<<<< HEAD
=======
>>>>>>> d39b1111855c5f27524537cff71fb61f0c69d79d
>>>>>>> 8bd4555d53a8a63815a66c30803b3a0eeb24591d
