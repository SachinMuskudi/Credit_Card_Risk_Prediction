<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CreditRisk AI - README</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    body {
      font-family: 'Inter', system-ui, sans-serif;
      background: linear-gradient(135deg, #0f172a 0%, #1e2937 100%);
      color: #e2e8f0;
      line-height: 1.7;
    }
    .hero-bg {
      background: linear-gradient(135deg, #1e40af, #3b82f6, #6366f1);
    }
    .glass {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .badge {
      background: rgba(255,255,255,0.15);
      color: white;
    }
  </style>
</head>
<body class="min-h-screen">

  <!-- Hero Section -->
  <div class="hero-bg text-white py-20 text-center">
    <div class="max-w-5xl mx-auto px-6">
      <div class="inline-flex items-center gap-3 bg-white/20 text-white text-sm font-semibold px-6 py-3 rounded-full mb-6">
        <i class="fas fa-shield-alt"></i>
        MACHINE LEARNING PROJECT
      </div>
      <h1 class="text-6xl font-bold mb-4 tracking-tight">CreditRisk AI</h1>
      <p class="text-2xl font-medium text-blue-100">Predicting Creditworthiness with Logistic Regression</p>
      <p class="mt-4 text-lg text-blue-200 max-w-2xl mx-auto">
        A complete end-to-end Machine Learning web application that predicts whether a customer is a <span class="font-semibold">"Good"</span> or <span class="font-semibold">"Bad"</span> credit risk.
      </p>
      
      <div class="flex justify-center gap-4 mt-10">
        <a href="#demo" class="inline-flex items-center gap-3 bg-white text-blue-700 font-semibold px-8 py-4 rounded-2xl hover:scale-105 transition">
          <i class="fas fa-play"></i> Live Demo
        </a>
        <a href="#features" class="inline-flex items-center gap-3 border border-white/50 font-semibold px-8 py-4 rounded-2xl hover:bg-white/10 transition">
          <i class="fas fa-star"></i> Features
        </a>
      </div>
    </div>
  </div>

  <div class="max-w-5xl mx-auto px-6 py-12">

    <!-- Tech Stack -->
    <div class="glass rounded-3xl p-8 mb-12">
      <h2 class="text-2xl font-bold mb-6 flex items-center gap-3">
        <i class="fas fa-tools"></i> Tech Stack
      </h2>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-white/10 rounded-2xl p-5 text-center">
          <i class="fas fa-flask text-4xl text-blue-400 mb-3"></i>
          <p class="font-semibold">Flask</p>
          <p class="text-sm text-gray-400">Backend</p>
        </div>
        <div class="bg-white/10 rounded-2xl p-5 text-center">
          <i class="fas fa-brain text-4xl text-purple-400 mb-3"></i>
          <p class="font-semibold">Scikit-learn</p>
          <p class="text-sm text-gray-400">Logistic Regression</p>
        </div>
        <div class="bg-white/10 rounded-2xl p-5 text-center">
          <i class="fas fa-chart-bar text-4xl text-emerald-400 mb-3"></i>
          <p class="font-semibold">Pandas & Numpy</p>
          <p class="text-sm text-gray-400">Data Processing</p>
        </div>
        <div class="bg-white/10 rounded-2xl p-5 text-center">
          <i class="fas fa-html5 text-4xl text-orange-400 mb-3"></i>
          <p class="font-semibold">HTML + Tailwind</p>
          <p class="text-sm text-gray-400">Modern UI</p>
        </div>
      </div>
    </div>

    <!-- Project Screenshot -->
    <div id="demo" class="mb-16">
      <h2 class="text-3xl font-bold mb-6 text-center">Live Web Interface</h2>
      <div class="glass rounded-3xl p-4 shadow-2xl">
        <img src="https://via.placeholder.com/1200x650/1e2937/60a5fa?text=CreditRisk+AI+Web+Application" 
             alt="CreditRisk AI Web App" class="rounded-2xl w-full shadow-inner">
      </div>
      <p class="text-center text-sm text-gray-400 mt-4">Beautiful, responsive prediction form with real-time results</p>
    </div>

    <!-- Features -->
    <div id="features" class="mb-16">
      <h2 class="text-3xl font-bold mb-8 text-center">Key Features</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div class="glass rounded-3xl p-8 hover:scale-105 transition">
          <i class="fas fa-database text-4xl text-blue-400 mb-4"></i>
          <h3 class="text-xl font-semibold mb-2">End-to-End ML Pipeline</h3>
          <p class="text-gray-400">Data cleaning, feature engineering, encoding, scaling, and model training.</p>
        </div>
        <div class="glass rounded-3xl p-8 hover:scale-105 transition">
          <i class="fas fa-globe text-4xl text-cyan-400 mb-4"></i>
          <h3 class="text-xl font-semibold mb-2">Interactive Web App</h3>
          <p class="text-gray-400">Deployed using Flask with a sleek, user-friendly interface.</p>
        </div>
        <div class="glass rounded-3xl p-8 hover:scale-105 transition">
          <i class="fas fa-chart-pie text-4xl text-emerald-400 mb-4"></i>
          <h3 class="text-xl font-semibold mb-2">Accurate Prediction</h3>
          <p class="text-gray-400">Logistic Regression model with proper preprocessing and feature selection.</p>
        </div>
      </div>
    </div>

    <!-- Project Structure -->
    <div class="glass rounded-3xl p-8 mb-12">
      <h2 class="text-3xl font-bold mb-6">Project Structure</h2>
      <pre class="bg-black/50 text-gray-300 p-6 rounded-2xl overflow-x-auto text-sm font-mono">
Credit Card Risk Prediction/
├── app.py                      # Flask Web Application
├── templates/index.html        # Beautiful Prediction UI
├── Model.pkl                   # Trained Logistic Regression Model
├── standard_scalar.pkl         # Fitted Scaler
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

    <!-- How to Run -->
    <div class="glass rounded-3xl p-10 mb-12">
      <h2 class="text-3xl font-bold mb-6 flex items-center gap-3">
        <i class="fas fa-terminal"></i> How to Run Locally
      </h2>
      <div class="space-y-4 text-lg">
        <div class="flex gap-4">
          <span class="bg-green-500/20 text-green-400 px-4 py-1 rounded-xl font-mono">1</span>
          <div>Clone the repository</div>
        </div>
        <div class="flex gap-4">
          <span class="bg-green-500/20 text-green-400 px-4 py-1 rounded-xl font-mono">2</span>
          <div>Install dependencies: <code class="bg-black/60 px-3 py-1 rounded">pip install -r requirements.txt</code></div>
        </div>
        <div class="flex gap-4">
          <span class="bg-green-500/20 text-green-400 px-4 py-1 rounded-xl font-mono">3</span>
          <div>Run the application: <code class="bg-black/60 px-3 py-1 rounded">python app.py</code></div>
        </div>
        <div class="flex gap-4">
          <span class="bg-green-500/20 text-green-400 px-4 py-1 rounded-xl font-mono">4</span>
          <div>Open browser at <span class="text-blue-400">http://127.0.0.1:5000</span></div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="text-center py-12 border-t border-white/10">
      <p class="text-2xl font-bold mb-2">Made with ❤️ for Credit Risk Analysis</p>
      <p class="text-gray-400">A complete Machine Learning + Web Development project</p>
      <div class="flex justify-center gap-6 mt-8 text-3xl">
        <i class="fab fa-python hover:text-yellow-400 cursor-pointer"></i>
        <i class="fas fa-flask hover:text-blue-400 cursor-pointer"></i>
        <i class="fas fa-brain hover:text-purple-400 cursor-pointer"></i>
      </div>
    </div>
  </div>

</body>
</html>
