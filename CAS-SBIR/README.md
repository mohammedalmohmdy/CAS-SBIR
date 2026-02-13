
# CAS-SBIR

Experimental protocol for:

Curriculum-Aware Abstraction-Guided Learning for Sketch-Based Image Retrieval (CAS-SBIR)

---

📂 Datasets

- **ShoeV2 / ChairV2**  
  [Sketchy Official Website](https://sketchx.eecs.qmul.ac.uk/downloads/)  
  [Google Drive Download](https://drive.google.com/file/d/1frltfiEd9ymnODZFHYrbg741kfys1rq1/view)

- **Sketchy**  
  [Sketchy Official Website](https://sketchx.eecs.qmul.ac.uk/downloads/)  
  [Google Drive Download](https://drive.google.com/file/d/11GAr0jrtowTnR3otyQbNMSLPeHyvecdP/view)

- **TU-Berlin**  
  [TU-Berlin Official Website](https://www.tu-berlin.de/)  
  [Google Drive Download](https://drive.google.com/file/d/12VV40j5Nf4hNBfFy0AhYEtql1OjwXAUC/view)

---

## Run Example

python main.py --config experiments/sketchy/config.yaml

This will:
1. Compute abstraction cache (if needed)
2. Train with curriculum learning
3. Evaluate full-gallery retrieval
4. Run 5 random seeds
5. Report mean ± std ± 95% CI
6. Save results to `outputs/`

---

## Metrics
- mAP
- Top-1
- Top-10
- P@10
- P@100

 Citation: If you use this code, please cite:

title = {Curriculum-Aware Abstraction-Guided Learning for Sketch-Based Image Retrieval (CAS-SBIR)},

author = {Mohammed A. S. Al-Mohamadi and Prabhakar C. J.},
Contact: almohmdy30@gmail.com GitHub: https://github.com/mohammedalmohmdy

journal = {...........}, year = {2026} }

Contact: almohmdy30@gmail.com GitHub: https://github.com/mohammedalmohmdy



