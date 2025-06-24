# README

## Background

Perturb-seq is a high-throughput screening technique used to investigate the effect of gene perturbations on transcriptomic readouts, specifically using single-cell RNA sequencing (scRNA-seq). In traditional setups:

- A **single gene** is perturbed (knocked out or turned off) in a cell.
- The **transcriptome** of that cell is sequenced, resulting in a vector of RNA read counts across ~20,000 genes.
- This process is repeated across many cells to infer **which genes are transcriptionally affected** by the specific gene perturbation.

These effects are expected to be **sparse**—i.e., only a small number of genes are altered by a given perturbation.

In this project, the experiment adds complexity by **perturbing multiple genes within each cell** using **guide-pooling Perturb-seq**:

- Each cell receives a **random combination of perturbations** (referred to as **composite samples**).
- Cells are then assayed with RNA-sequencing.
- This method is more **cost-effective**, allows learning of **individual perturbation effects**, and offers insights into **higher-order genetic interactions**.

## Data

The dataset consists of:

- **Expression matrix `X`**: A genes × cells RNA-seq matrix representing the number of RNA reads per gene per cell.
- **Perturbation matrix `Z`**: A cells × sgRNA indicator matrix representing whether a given cell has a perturbation in a given gene.

### Properties of the Data

1. Most gene perturbations affect a small number of genes.
2. The RNA read count matrix is **sparse** due to technical limitations; zeros may indicate either true absence or dropout.
3. Only a few latent features are expected to explain transcriptomic expression in any given cell.

## Motivation / Project Goals

The core goal is to infer the effect of a **single gene perturbation** on the transcriptome from composite samples generated in guide-pooling Perturb-seq screens. Specifically:

- **Deconvolve** multiple perturbation signals in each cell to determine individual perturbation effects.
- Previous work (Yao et al., 2023) used **compressed sensing** methods involving:
  - Sparse PCA (sPCA)
  - Lasso regression
  - Evaluation against unpooled Perturb-seq ground truth

This project proposes an alternative approach using **dictionary learning**:

- Reduces dimensionality while promoting **sparsity** in a biologically interpretable manner.
- Produces **interpretable latent features** more effectively than PCA or ICA (Pan et al., 2022).
- Will explore both **l0 and l1 regularization** on the sparse code, and optionally on the dictionary.
- Will apply **lasso or least squares regression** to compute perturbation effect sizes.

An additional post-analysis step will involve:

- Using the matrix `Z` to create a **cell-cell similarity graph**.
- Regularizing the sparse code matrix with graph-based priors (inspired by Pan et al.).

The regression problems will be solved using:

- **Autoencoder frameworks**
- Or **alternating minimization algorithms**

### One-Step Estimation

As an additional aim, the project will also explore computing transcriptomic effect sizes in a **single step**:

- Use dictionary learning where the **number of latent features equals the number of genes perturbed**.
- Regularize the support of the sparse code to match perturbations in `Z`.

## Tools Implemented

- Backpropogation
- Regression
- Dimensionality Reduction
- Dictionary Learning
- Autoencoders / Alternating Minimization Algorithm
