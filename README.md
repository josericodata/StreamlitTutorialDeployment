# 🍩 Streamlit Tutorial Deployment
In this step-by-step tutorial, you will learn how to deploy your Streamlit App in just a few minutes 🚀.

---

# 🔑 Why am I making this tutorial?
When I first started creating Streamlit apps, I had no idea how to link my GitHub repository to Streamlit or even where to begin. Hopefully, this tutorial will help someone out there who is in the same situation.<br>
Additionally, I’ll be creating a series of videos about my Streamlit apps, and this video serves as the starting point if you want to follow along. This will be especially useful if you’d like to clone the repository and tweak the app locally.

---

# 🧬 Tutorial structure

This tutorial is divided in three parts:

## 1. From local to GitHub
I’ll show you how to create a GitHub repository and push your developed app to the newly created repository.

## 2. Deploying the app into Streamlit
Once the app is hosted in your GitHub repository, deploying it on Streamlit is the easy part. I’ll guide you through the process step by step.

## 3. Cloning the app from GitHub and running it locally
Now, we’ll reverse the process. Imagine you find a Streamlit app that interests you and want to clone it to experiment with it locally. I’ll show you how.

---

## 🛠️ **How It's Built**  

This app is built entirely using **Streamlit**, a Python framework that makes it easy to create and share interactive web applications.  

### **What the App Does**  
The app is a fun and interactive **Homer Simpson Donut Tracker**, where Homer eagerly eats donuts as they are thrown at him. It works as follows:  

1. **Initial State** – Homer appears hungry, waiting for donuts.  
2. **Throwing Donuts** – When you press the *Start Throwing Donuts* button, donuts begin moving across the screen toward Homer’s mouth. The app tracks how many donuts he eats.  
3. **Stopping the Feast** – When you press *Stop Throwing Donuts*, the animation stops, and Homer reacts with disappointment, displaying a sad GIF.  

### **Why Streamlit?**  
Streamlit allows us to create this engaging app with minimal code. We use:  
- **Buttons** to start and stop the donut animation.  
- **Session State** to track Homer’s donut count and update his expressions dynamically.  
- **GIFs and Images** to animate Homer’s emotions.  
- **Custom Styling** to give the app a fun, Simpsons-themed design.  

With just **one library—Streamlit**, we’ve built an interactive app that is both simple and visually engaging! 👌

---

## 🚀 **Getting Started**

### **From local to GitHub**

1. Clone the repository:
```bash
git clone https://github.com/josericodata/StreamlitTutorialDeployment.git
```

2. Navigate to the repository directory:
```bash
cd StreamlitTutorialDeployment
```

3. Check current remote URL:
```bash
git remote -v
```
If it shows HTTPS (https://github.com/...), update it to SSH:

4. Set the remote URL:
```bash
git remote set-url origin git@github.com:josericodata/StreamlitTutorialDeployment.git
```

**Note:** I'm using my user `git@github.com:josericodata`, when you are replicating you will be using your user name `git@github.com:yourusername`, keep that in mind.

5. Check again current remote URL:
```bash
git remote -v
```
You should now see:

`origin  git@github.com:josericodata/StreamlitTutorialDeployment.git(fetch)`<br>
`origin  git@github.com:josericodata/StreamlitTutorialDeployment.git (push)`

**Note:** Now it is showing my user `git@github.com:josericodata`, when you are replicating it you should see `git@github.com:yourusername`, keep that in mind.

6. Ping the repository:
```bash
ssh -T git@github.com
```

You should get this message: **Hi josericodata! You've succesfully authenticated, but GitHub does not provide shell access.**<br>

Now it's the moment to add your developed app into StreamlitTutorialDeployment, copy and paste the files and commit the changes to GitHub.

7. Add the files:
```bash
git add .
```

8. Commit changes:
```bash
git commit -m"Uploading Your Streamlit App."
```

9. Push changes into GitHub:
```bash
git push origin main
```
Check now your GitHub repository you should see the a new commit there.

### **Cloning the app from GitHub and running it locally**

In the video, you can see that I'm creating a new directory. This is because I'm cloning the same app I developed, so I need to move to a different location to avoid any conflicts.
If you're following this tutorial step by step, simply create a new directory and clone the app there.

1. Clone the repository:
```bash
git clone https://github.com/user/StreamlitTutorialDeployment.git
```
**Hint:** Replace `user` with `josericodata` in the URL above. I am deliberately asking you to pause here so you can support my work. If you appreciate it, please consider giving the repository a star or forking it. Your support means a lot—thank you! 😊

2. Navigate to the repository directory:
```bash
cd StreamlitTutorialDeployment
```

2. Navigate to the repository directory:
```bash
python3 -m venv venvStrTutDep
```

3. Activate the virtual environment:
```bash
source venvStrTutDep/bin/activate
```

4. Install requirements:
```bash
pip install -r requirements.txt
```

5. Navigate to the app directory:
```bash
cd streamlit_app
```

6. Run the app:
```bash
streamlit run app.py
```

The app will be live at ```http://localhost:8501```

---

## 🎬 **Demo**
  
### Tutorial deployment Streamlit app:
![Homer Eating Donuts](https://raw.githubusercontent.com/josericodata/StreamlitTutorialDeployment/main/streamlit_app/assets/gifs/homer.gif)

---

### ▶️ Watch the YouTube Tutorial


[![How to Deploy Your Streamlit App in Just Minutes Complete Tutorial Guide](https://img.youtube.com/vi/6fTxRzDErbc/maxresdefault.jpg)](https://www.youtube.com/watch?v=6fTxRzDErbc "Click to play")

Click the image above or [here](https://www.youtube.com/watch?v=6fTxRzDErbc) to watch the video on YouTube.

---

## 🔧 **Environment Setup**

The Streamlit Tutorial Deployment app is built and tested using the following software environment:

- **Operating System**: Ubuntu 22.04.5 LTS (Jammy)
- **Python Version**: Python 3.10.12

---

### ⚠️ **Disclaimer**  
This tutorial is intended for educational purposes only. While I have done my best to ensure accuracy, I cannot guarantee that everything will work flawlessly in every environment.  

Deploying a Streamlit app depends on external services like GitHub and Streamlit, which may change over time. If you encounter any issues, please refer to the official documentation of these platforms.  

Use this tutorial as a guide, but always verify configurations and security settings, especially when deploying real-world applications. I am not responsible for any issues that arise from following this tutorial.  

Happy coding! 🚀  

