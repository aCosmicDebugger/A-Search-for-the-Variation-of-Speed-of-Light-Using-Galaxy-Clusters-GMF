# A Search for the variation of the speed of light using galaxy clusters gas mass fraction
measurements   
[![DOI](https://zenodo.org/badge/DOI/10.1088/1475-7516/2021/10/084.svg)](https://doi.org/10.1088/1475-7516/2021/11/034)
[![Inspire HEP](https://img.shields.io/badge/Inspire-HEP-orange)](https://inspirehep.net/literature/1933934)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--7182--7273-green)](https://orcid.org/0000-0001-7182-7273)



In this paper, we propose a new model-independent method to test the invariance of the speed of
light c by combining the galaxy cluster observations, H(z) measurements from cosmic chronometers,
and the observations of type-Ia supernovae (SNe Ia). In our analyses, we consider both a constant
depletion factor (which corresponds to the ratio by which fgas is depleted with respect to the
universal baryonic mean) and one varying with redshift. We also consider the influence of different
H0 estimates on our results.

We achieve this by employing Gaussian Processes Regression (GPR) to reconstruct the luminosity distance for 3 different priors on $H_{0}$. One for a H_{0} estimate using
a model-independent measure of H(z) called Cosmic Chronometers, for another prior on $H_{0}$ we use the Planck best-fit of CMB and finally the prior of $H_{0}$ using Ries measurements. We maximize the likelihoods for 2 distinct models: (i) a model with  varying c, $c \equiv c(z) = 1 + c_{1}z$ with a constant depletion factor, (ii) a model with a varying c $c\equiv c(z) = (1 + c{1}z)$ with a depletion factor $\gamma (z) = (1+\gamma_{1}z)$. 

And our results are summarized in the table:

## Constraints on the parameter $c_1$

| **Distance Indicator**                   | $\gamma(z)$ considered | **$\gamma_1$**             | **$c_1$**              |
|-----------------------------------------|------------------------|----------------------------|------------------------|
| Cosmic Chronometers                     | $0.85\pm0.08$          | -                          | $-0.069\pm0.056$      |
| Cosmic Chronometers                     | $0.85(1+\gamma_1z)$    | $0.009^{+0.45}_{-0.366}$    | $-0.076\pm0.262$      |
| Pantheon Sample with Planck $H_0$ prior | $0.85\pm0.08$          | -                          | $-0.016\pm0.055$      |
| Pantheon Sample with Planck $H_0$ prior | $0.85(1+\gamma_1z)$    | $0.061^{+0.523}_{-0.426}$  | $-0.054\pm0.301$      |
| Pantheon Sample with Riess $H_0$ prior   | $0.85\pm0.08$          | -                          | $-0.198\pm0.052$      |
| Pantheon Sample with Riess $H_0$ prior   | $0.85(1+\gamma_1z)$    | $-0.097^{+0.298}_{-0.249}$ | $-0.141\pm0.178$     |

For more details on my publication, see: [arXiv](https://arxiv.org/abs/2109.14512v1).
Export citation:
<div style="background-color: Snow; padding: 10px; margin-top: 10px;">
    <a href="https://htmlpreview.github.io/?https://github.com/aCosmicDebugger/Galaxy-Clusters-Cosmic-Chronometers-EEP/blob/main/bibtex.html" style="color: MidnightBlue;">bibtex.txt</a>
</div>



## Tools Used:


- ![Python](https://img.shields.io/badge/Python-3.11-blue)
- ![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-5.3.0-orange)
- ![Sci-Kit Learn](https://img.shields.io/badge/Sci--Kit%20Learn-1.2.2-yellow)
- ![emcee](https://img.shields.io/badge/emcee-3.1.4-green)
- ![corner.py](https://img.shields.io/badge/corner.py-2.2.2-cerulean)




Feel free to explore the code and analysis in the associated files.

