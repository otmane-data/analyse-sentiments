# 🏨 Hotel Sentiment Analysis API 🌟

## 📋 Project Description

This project is a sentiment analysis API that predicts whether a hotel is recommended based on user comments. It uses machine learning to classify comments as positive or negative and provides an overall recommendation.

## 🏗️ Project Structure

<pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">Code</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-"><div class="overflow-x-auto bg-editor-content-area p-3"><code node="[object Object]" aria-label="plain-code-" class="text-sm">project_root/
│
├── app/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── final_nb_pipeline.joblib
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
└── code.ipynb</code></div></div></div></pre>

## 🛠️ Technologies Used

* **FastAPI** 🚀: Modern, fast web framework for building APIs
* **Python** 🐍: Primary programming language
* **scikit-learn** 🧠: Machine learning library for the sentiment analysis model
* **joblib** 💾: Used for model serialization and loading
* **NumPy** 🔢: Numerical computing library
* **Docker** 🐳: Containerization for easy deployment
* **Jupyter Notebook** 📓: Used for data analysis and model development

## 🔌 API Endpoints

1. **GET /**
   * Welcome message
   * Response: `{'message': 'analyse_sentiment model API'}`
2. **GET /testing**
   * Test endpoint
   * Response: `{'message': 'analyse_sentiment model API'}`
3. **POST /recommend**
   * Main sentiment analysis endpoint
   * Input: JSON with a 'sentences' key containing an array of comments
   * Output: Sentiment analysis results and recommendation

## 🧠 Machine Learning Model

* **Type** : Naive Bayes classifier
* **Features** : TF-IDF vectorized text
* **Classes** : Positive and Negative sentiment

## 🚀 Getting Started

1. **Clone the repository**
   <pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">Code</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-"><div class="overflow-x-auto bg-editor-content-area p-3"><code node="[object Object]" aria-label="plain-code-" class="text-sm">git clone <repository-url>
   cd <project-directory></code></div></div></div></pre>
2. **Install dependencies**
   <pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">Code</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-"><div class="overflow-x-auto bg-editor-content-area p-3"><code node="[object Object]" aria-label="plain-code-" class="text-sm">pip install -r app/requirements.txt</code></div></div></div></pre>
3. **Build the Docker image**
   <pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">Code</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-"><div class="overflow-x-auto bg-editor-content-area p-3"><code node="[object Object]" aria-label="plain-code-" class="text-sm">docker build -t hotel-sentiment-api ./app</code></div></div></div></pre>
4. **Run the Docker container**
   <pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">Code</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-"><div class="overflow-x-auto bg-editor-content-area p-3"><code node="[object Object]" aria-label="plain-code-" class="text-sm">docker run -p 8000:8000 hotel-sentiment-api</code></div></div></div></pre>
5. **Access the API**
   * The API will be available at `http://localhost:8000`

## 📊 Usage Example

**Request:**

<pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">json</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="language-json relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-language-json"><div class="w-full overflow-x-auto"><div><code><span>POST /recommend
</span><span></span><span class="token">{</span><span>
</span><span></span><span class="token">"sentences"</span><span class="token">:</span><span></span><span class="token">[</span><span>
</span><span></span><span class="token">"The hotel was amazing, great service!"</span><span class="token">,</span><span>
</span><span></span><span class="token">"Room was dirty and staff was rude."</span><span>
</span><span></span><span class="token">]</span><span>
</span><span></span><span class="token">}</span></code></div></div></div></div></pre>

**Response:**

<pre><div><div class="relative -mb-[1px] flex flex-row items-center justify-between rounded-t border border-gray-700 px-2 py-0.5"><div class="absolute inset-0 bg-gray-500 opacity-20"></div><div class="font-sans text-sm text-ide-text-color">json</div><div><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-ide-text-color font-sans hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div></div><div class="language-json relative box-border overflow-hidden rounded-[0.25em] border border-gray-700" aria-label="highlighted-code-language-json"><div class="w-full overflow-x-auto"><div><code><span class="token">{</span><span>
</span><span></span><span class="token">"total_comments"</span><span class="token">:</span><span></span><span class="token">2</span><span class="token">,</span><span>
</span><span></span><span class="token">"positive_comments"</span><span class="token">:</span><span></span><span class="token">1</span><span class="token">,</span><span>
</span><span></span><span class="token">"positive_percentage"</span><span class="token">:</span><span></span><span class="token">50.0</span><span class="token">,</span><span>
</span><span></span><span class="token">"is_recommended"</span><span class="token">:</span><span></span><span class="token">false</span><span>
</span><span></span><span class="token">}</span></code></div></div></div></div></pre>

## 📝 Logging

The API uses Python's logging module to log information and errors. Check the console output for logs.

## 🛠️ Development

The `code.ipynb` Jupyter notebook contains the data analysis, model training, and evaluation process. Refer to this notebook for insights into the model development.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/ADmiN/.vscode/extensions/codeium.codeium-1.30.2/dist/LICENSE).

---

Created with ❤️ by Otmane Aghzar
