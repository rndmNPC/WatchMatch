# Roadmap

## Milestone 1 - Image foundations

- [x] Python 3.12 environment works
- [x] image metadata loader with tests
- [x] resize and RGB conversion with tests
- [ ] NumPy array shapes and value ranges documented

## Milestone 2 - Small catalog

- [ ] legally usable or self-created image source selected
- [ ] 100-300 images organized with minimal labels
- [ ] metadata validation script
- [ ] train/validation/test split without duplicate leakage

## Milestone 3 - ResNet50 baseline

- [ ] pretrained weights and preprocessing understood
- [ ] embeddings generated without gradient tracking
- [ ] cosine similarity implemented and tested
- [ ] top-5 retrieval demo works locally
- [ ] latency and baseline retrieval metric recorded

## Milestone 4 - CLIP comparison

- [ ] equivalent CLIP embeddings generated
- [ ] same evaluation split used
- [ ] Recall@K and qualitative failure cases compared
- [ ] model choice documented with evidence

## Milestone 5 - Product surface

- [ ] FastAPI query endpoint
- [ ] React upload and results view
- [ ] errors and loading states handled
- [ ] end-to-end test

## Milestone 6 - Shipping and evidence

- [ ] Docker setup
- [ ] CI runs tests
- [ ] public demo or reproducible local demo
- [ ] five user tests
- [ ] README with architecture, limitations and measured results
- [ ] short demo video
