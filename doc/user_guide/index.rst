**********
User Guide
**********

Getting Started
---------------

.. Must use a raw element with an object tag for clickable links. https://stackoverflow.com/a/35562792

.. raw:: html

    <object data="../_static/user_guide.svg" type="image/svg+xml" width="900"></object>


Creating and working with an AnnotatedGEM
-----------------------------------------

* `AnnotatedGEM from pandas <AnnotatedGEM_from_pandas.ipynb>`_
  How to load your count and label .csv or .txt files into an `xarray.Dataset` using `GSForge`, and save them as a single netcdf (.nc) file for future use.

* `GEM Normalization <GEM_Normalization.ipynb>`_
  How to run and save different normalizations to the same `AnnotatedGEM` object.


Selecting Genes & Creating a GeneSet
------------------------------------

* `Selecting Genes with Boruta <Selecting_Genes_with_Boruta.ipynb>`_
  How to select genes based on a sample label using random forests via the Boruta algorithm.


Creating a GeneSetCollection and Analyzing Results
--------------------------------------------------

* `GeneSet Analysis <GeneSet_Analysis.ipynb>`_
  How to run a basic gene (feature) selection using random forests and the Boruta all-relevant feature selection algorithm.


Other Guides
------------

* `Plotting Guide <plotting_guide/index.rst>`_
  Plotting examples by plot type.

* `Workflow Guide <workflow_guide/index.rst>`_
  Using nextflow to run many different boruta analyses.

* `R-Integration Guide <R_integration_guide/index.rst>`_
  Integrating results from R packages into GeneSet objects.



.. toctree::
    :titlesonly:
    :maxdepth: 2

    Plotting Gallery <plotting_guide_gallery/index>
    AnnotatedGEM from pandas <AnnotatedGEM_from_pandas>
    GEM Normalization <GEM_Normalization>
    Selecting Genes with Boruta <Selecting_Genes_with_Boruta>
    GeneSet Analysis <GeneSet_Analysis>
    Plotting Guide <plotting_guide/index>
    Workflow Guide <workflow_guide/index>
    R-Integration Guide <R_integration_guide/index>
