
# CAS-SBIR

Experimental protocol for:

Curriculum-Aware Abstraction-Guided Learning for Sketch-Based Image Retrieval (CAS-SBIR)

---

## Datasets
- Sketchy (Extended)
- QMUL-Shoe
- TU-Berlin

Official splits are used.

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



