# 🧠 IntelliLearn — CS3613 AI Study Platform (Web Edition)

> Reverse-engineered from `IntelliLearn-debug.apk` (`com.chamath.intellilearn`).  
> An interactive web-based study platform for **CS3613: Introduction to Artificial Intelligence**.

---

## 🚀 Quick Start

### Option 1: 1-Click Launch (Windows)
Double-click [`start.bat`](file:///C:/Users/Dilantha/.gemini/antigravity/scratch/intellilearn-web/start.bat). It will launch the local HTTP server and automatically open your default browser.

### Option 2: Python
```bash
python serve.py
```
Opens at [http://localhost:3613](http://localhost:3613).

### Option 3: Node.js / NPM
```bash
npm start
# or
npx serve -l 3613
```

---

## 🔍 Reverse Engineering Analysis

| Attribute | Extracted APK Finding | Web Adaptation |
|---|---|---|
| **App Identity** | `com.chamath.intellilearn` (v1.0.0 Debug) | IntelliLearn Web Platform |
| **Framework** | Capacitor 7.x + React 18 + Vite | Pure Single-Page Application (SPA) |
| **Routing** | React Router v7 (`HashRouter`) | Hash-based (`/#/`, `/#/learn`, `/#/ready`) — works on any static host |
| **Styling** | Tailwind CSS v4.3.3 | Fully preserved (`assets/index-DT9r9Ls0.css`) |
| **Math Engine** | KaTeX (TeX / LaTeX typesetting) | Local KaTeX web fonts (`.woff2`, `.woff`, `.ttf`) |
| **Slide Rendering** | React-Markdown + Remark + Rehype | Dynamic fetch of `./docs/{doc}/p{page}.md` + companion `.jpg` |
| **Data Storage** | `localStorage` key `intellilearn.v1` | Retains user progress, mastery status, and mock exam scores |
| **Native Plugins** | `capacitor.plugins.json` is `[]` (empty) | No native Android bridge dependencies! |

---

## 📚 Course Modules & Content Catalog

### 1. Learning Quizzes (14 Topics)
Interactive questions with single-choice, multiple-choice, diagrams, step-by-step explanations, citation links, and option-specific feedback:
1. **Intelligent Agents** (`agents`)
2. **Search** (`search`)
3. **Local Search & Optimization** (`local`)
4. **Constraint Satisfaction Problems** (`csp`)
5. **Adversarial Search** (`adversarial`)
6. **Game Theory** (`gametheory`)
7. **Propositional Logic** (`propositional`)
8. **First-Order Logic** (`fol`)
9. **FOL Inference** (`fol-inference`)
10. **Planning & Knowledge Representation** (`planning`)
11. **Probability & Uncertainty** (`probability`)
12. **Bayesian Networks** (`bayesnets`)
13. **Markov Decision Processes** (`mdp`)
14. **Reinforcement Learning** (`rl`)

### 2. Exam Readiness Papers (5 Timed Mock Exams)
10 questions each, 20-minute countdown timer, mixed MCQ and written questions with self-marking and model answers:
- **Paper 1**: Logic & FOL Inference (Resolution, CNF, Unification, Chaining)
- **Paper 2**: Search & Heuristics (Uninformed/informed search, A*, Local search, Genetic algorithms)
- **Paper 3**: CSP & Adversarial Search (Arc consistency, Minimax, Alpha-Beta pruning)
- **Paper 4**: Probability & Bayesian Networks (Bayes' Rule, CPT, Factorization, Independence)
- **Paper 5**: Mixed Exam Simulation + Agents, MDP & Reinforcement Learning

### 3. Integrated Slide & Textbook Viewer (650+ Pages)
Clicking any citation (e.g. `[Slide 35](cite:logic2:35)` or `[AIMA p.308](cite:aima:308)`) automatically opens the slide drawer side-by-side with the question, displaying the rendered markdown content and the lecture slide graphic.

---

## 🌐 Free Web Hosting & Deployment

Because the application uses `HashRouter` and relative paths (`./assets/...`, `./docs/...`, `./img/...`), you can deploy this directory to any static web host with zero backend configuration:

### Deploy to GitHub Pages
1. Push this folder to a GitHub repository.
2. In repository settings: **Pages** → Source: **Deploy from a branch** (`main` / root).
3. Your site is live!

### Deploy to Vercel
```bash
npx vercel deploy --prod
```
*(Pre-configured with `vercel.json`)*

### Deploy to Netlify
```bash
npx netlify deploy --prod --dir .
```
*(Pre-configured with `netlify.toml`)*

