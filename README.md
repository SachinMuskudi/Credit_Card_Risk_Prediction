<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>CreditRisk AI - README</title>

  <script src="https://cdn.tailwindcss.com"></script>

  <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"/>

  <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      scroll-behavior:smooth;
    }

    body{
      font-family:'Poppins',sans-serif;
      background:#020617;
      color:white;
      overflow-x:hidden;
    }

    body::before{
      content:'';
      position:fixed;
      width:700px;
      height:700px;
      background:#2563eb20;
      filter:blur(150px);
      top:-200px;
      left:-200px;
      z-index:-1;
    }

    body::after{
      content:'';
      position:fixed;
      width:700px;
      height:700px;
      background:#7c3aed20;
      filter:blur(150px);
      bottom:-200px;
      right:-200px;
      z-index:-1;
    }

    .hero{
      min-height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      text-align:center;
      padding:80px 20px;
      position:relative;
      background:
      radial-gradient(circle at top left,#2563eb25,transparent 30%),
      radial-gradient(circle at bottom right,#7c3aed25,transparent 30%),
      linear-gradient(135deg,#020617,#0f172a,#111827);
    }

    .glass{
      background:rgba(255,255,255,0.06);
      border:1px solid rgba(255,255,255,0.08);
      backdrop-filter:blur(16px);
      box-shadow:0 10px 40px rgba(0,0,0,0.45);
    }

    .gradient-text{
      background:linear-gradient(to right,#60a5fa,#818cf8,#38bdf8);
      -webkit-background-clip:text;
      -webkit-text-fill-color:transparent;
    }

    .floating{
      animation:floating 5s ease-in-out infinite;
    }

    @keyframes floating{
      0%{transform:translateY(0px);}
      50%{transform:translateY(-12px);}
      100%{transform:translateY(0px);}
    }

    .glow{
      box-shadow:0 0 45px rgba(59,130,246,0.45);
    }

    .card{
      transition:0.4s ease;
    }

    .card:hover{
      transform:translateY(-10px) scale(1.03);
      box-shadow:0 20px 50px rgba(59,130,246,0.25);
    }

    .section-title{
      font-size:3rem;
      font-weight:800;
      margin-bottom:3rem;
      text-align:center;
    }

    .terminal{
      background:#000;
      border:1px solid rgba(255,255,255,0.08);
    }

  </style>

</head>

<body>

  <!-- HERO SECTION -->

  <section class="hero">

    <div class="max-w-7xl mx-auto">

      <div
        class="inline-flex items-center gap-3 px-6 py-3 rounded-full glass text-blue-300 font-semibold text-sm mb-8 floating">

        <i class="fa-solid fa-shield-halved"></i>
        MACHINE LEARNING PROJECT

      </div>

      <h1 class="text-7xl md:text-8xl font-extrabold leading-tight mb-6 gradient-text floating">

        CreditRisk AI

      </h1>

      <p class="text-2xl md:text-3xl text-blue-100 font-semibold mb-6">

        Predicting Creditworthiness with Logistic Regression

      </p>

      <p class="max-w-4xl mx-auto text-lg md:text-xl text-slate-300 leading-relaxed">

        A complete end-to-end Machine Learning web application that predicts whether a customer is a
        <span class="text-emerald-400 font-bold">"Good"</span>
        or
        <span class="text-red-400 font-bold">"Bad"</span>
        credit risk.

      </p>

      <!-- BADGES -->

      <div class="flex flex-wrap justify-center gap-4 mt-12">

        <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"/>
        <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask"/>
        <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn"/>
        <img src="https://img.shields.io/badge/TailwindCSS-Modern_UI-06B6D4?style=for-the-badge&logo=tailwindcss"/>
        <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>

      </div>

      <!-- BUTTONS -->

      <div class="flex flex-wrap justify-center gap-5 mt-14">

        <a href="#demo"
          class="px-8 py-4 rounded-2xl bg-blue-500 hover:bg-blue-600 font-semibold text-white glow transition duration-300">

          <i class="fa-solid fa-play mr-2"></i>
          Live Demo

        </a>

        <a href="#features"
          class="px-8 py-4 rounded-2xl border border-slate-600 hover:border-blue-400 hover:bg-blue-500/10 font-semibold transition duration-300">

          <i class="fa-solid fa-star mr-2"></i>
          Features

        </a>

      </div>

      <!-- TECH ICONS -->

      <div class="mt-16">

        <img src="https://skillicons.dev/icons?i=python,flask,html,css,tailwind,github,vscode"/>

      </div>

    </div>

  </section>

  <!-- MAIN CONTENT -->

  <main class="max-w-7xl mx-auto px-6 py-20">

    <!-- ABOUT -->

    <section class="mb-28">

      <h2 class="section-title gradient-text">

        🌟 About The Project

      </h2>

      <div class="grid lg:grid-cols-2 gap-10 items-center">

        <div class="glass rounded-[35px] p-10">

          <h3 class="text-4xl font-bold mb-6">

            🚀 CreditRisk AI

          </h3>

          <p class="text-slate-300 text-lg leading-relaxed mb-6">

            An advanced Machine Learning based Credit Risk Prediction System built using
            Python, Flask, and Scikit-Learn.

          </p>

          <ul class="space-y-4 text-lg">

            <li>✅ Predict Good or Bad Credit Risk</li>
            <li>📊 Feature Engineering Pipeline</li>
            <li>⚡ Real-Time Prediction System</li>
            <li>🌐 Flask Web Application</li>
            <li>☁️ Deployment Ready Architecture</li>

          </ul>

        </div>

        <div class="flex justify-center">

          <img
            src="https://cdn-icons-png.flaticon.com/512/4727/4727496.png"
            class="w-[350px] floating glow"/>

        </div>

      </div>

    </section>

    <!-- TECH STACK -->

    <section class="mb-28">

      <h2 class="section-title gradient-text">

        ⚙️ Tech Stack

      </h2>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">

        <div class="glass rounded-[30px] p-10 text-center card">

          <i class="fa-solid fa-flask text-6xl text-blue-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-3">

            Flask

          </h3>

          <p class="text-slate-400">

            Backend Framework

          </p>

        </div>

        <div class="glass rounded-[30px] p-10 text-center card">

          <i class="fa-solid fa-brain text-6xl text-purple-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-3">

            Scikit-Learn

          </h3>

          <p class="text-slate-400">

            Logistic Regression

          </p>

        </div>

        <div class="glass rounded-[30px] p-10 text-center card">

          <i class="fa-solid fa-chart-column text-6xl text-emerald-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-3">

            Pandas & Numpy

          </h3>

          <p class="text-slate-400">

            Data Processing

          </p>

        </div>

        <div class="glass rounded-[30px] p-10 text-center card">

          <i class="fa-brands fa-html5 text-6xl text-orange-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-3">

            HTML + Tailwind

          </h3>

          <p class="text-slate-400">

            Modern UI

          </p>

        </div>

      </div>

    </section>

    <!-- LIVE UI -->

    <section id="demo" class="mb-28">

      <h2 class="section-title gradient-text">

        🌐 Live Web Interface

      </h2>

      <div class="glass rounded-[40px] p-5 glow">

        <img
          src="https://via.placeholder.com/1200x650/0f172a/60a5fa?text=CreditRisk+AI+Web+Application"
          class="rounded-[30px] w-full"/>

      </div>

      <p class="text-center text-slate-400 mt-5 text-lg">

        Beautiful, responsive prediction form with real-time results

      </p>

    </section>

    <!-- FEATURES -->

    <section id="features" class="mb-28">

      <h2 class="section-title gradient-text">

        🔥 Key Features

      </h2>

      <div class="grid md:grid-cols-3 gap-8">

        <div class="glass rounded-[30px] p-10 card">

          <i class="fa-solid fa-database text-6xl text-blue-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-4">

            End-to-End ML Pipeline

          </h3>

          <p class="text-slate-400 text-lg">

            Data cleaning, feature engineering, encoding, scaling & model training.

          </p>

        </div>

        <div class="glass rounded-[30px] p-10 card">

          <i class="fa-solid fa-globe text-6xl text-cyan-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-4">

            Interactive Web App

          </h3>

          <p class="text-slate-400 text-lg">

            Deployed using Flask with modern & attractive UI.

          </p>

        </div>

        <div class="glass rounded-[30px] p-10 card">

          <i class="fa-solid fa-chart-pie text-6xl text-emerald-400 mb-6"></i>

          <h3 class="text-2xl font-bold mb-4">

            Accurate Prediction

          </h3>

          <p class="text-slate-400 text-lg">

            Logistic Regression model with proper preprocessing.

          </p>

        </div>

      </div>

    </section>

    <!-- STRUCTURE -->

    <section class="mb-28">

      <h2 class="section-title gradient-text">

        📂 Project Structure

      </h2>

      <div class="terminal rounded-[35px] p-10 overflow-x-auto">

<pre class="text-slate-300 text-sm md:text-base leading-loose">
Credit Card Risk Prediction/
├── app.py                      # Flask Web Application
├── templates/
│   └── index.html              # Beautiful Prediction UI
├── Model.pkl                   # Trained Logistic Regression Model
├── standard_scalar.pkl         # Fitted Standard Scaler
├── creditcard.csv              # Original Dataset
├── All_Models.py               # Model Experimentation
├── feature_scaling.py
├── Categorical_to_num.py
├── filter_methods.py
├── Random_Sample_Imputation.py
├── main.py
├── requirements.txt
└── Documentation files...
</pre>

      </div>

    </section>

    <!-- HOW TO RUN -->

    <section class="mb-28">

      <div class="glass rounded-[40px] p-12">

        <h2 class="section-title gradient-text">

          🚀 How to Run Locally

        </h2>

        <div class="space-y-8 text-lg">

          <div class="flex gap-5 items-start">

            <div
              class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-2xl">

              1

            </div>

            <div class="text-xl">

              Clone the repository

            </div>

          </div>

          <div class="flex gap-5 items-start">

            <div
              class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-2xl">

              2

            </div>

            <div class="text-xl">

              Install dependencies:

              <code class="bg-black/60 px-4 py-2 rounded-xl ml-2">
                pip install -r requirements.txt
              </code>

            </div>

          </div>

          <div class="flex gap-5 items-start">

            <div
              class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-2xl">

              3

            </div>

            <div class="text-xl">

              Run the application:

              <code class="bg-black/60 px-4 py-2 rounded-xl ml-2">
                python app.py
              </code>

            </div>

          </div>

          <div class="flex gap-5 items-start">

            <div
              class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-2xl">

              4

            </div>

            <div class="text-xl">

              Open

              <span class="text-blue-400 font-semibold">

                http://127.0.0.1:5000

              </span>

              in your browser

            </div>

          </div>

        </div>

      </div>

    </section>

    <!-- FOOTER -->

    <footer class="text-center py-20 border-t border-white/10">

      <h2 class="text-5xl font-extrabold gradient-text mb-5">

        ❤️ Made with Passion for Credit Risk Analysis

      </h2>

      <p class="text-slate-400 text-xl">

        A complete Machine Learning + Full Stack Web Development Project

      </p>

      <div class="flex justify-center gap-5 mt-10">

        <i class="fa-brands fa-python text-4xl text-yellow-400"></i>
        <i class="fa-solid fa-brain text-4xl text-purple-400"></i>
        <i class="fa-solid fa-globe text-4xl text-cyan-400"></i>
        <i class="fa-solid fa-chart-line text-4xl text-emerald-400"></i>

      </div>

    </footer>

  </main>

</body>

</html>
