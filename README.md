# Reproducible Brain Charts Analysis Template

This repo can be used as a template for creating new repos that will
process RBC datasets. It has some useful scripts to get started in
the `code/` directory.

## Getting started

Create a new repository, selecting this repo as a template on the
github website.
**It is required that you include all the branches in your new repo.**

Suppose you created a new repo called `ReproBrainChart/ExampleAnalysis.git`.
You will clone this repo with datalad using

```bash
datalad clone git@github.com:ReproBrainChart/ExampleAnalysis.git
```

This will create an `ExampleAnalysis` directory that is ready to start
analyzing RBC data.

### Installing RBC datasets

There are some convenience scripts included in this template to get you started.
Suppose I want to get the structural and functional from the CCNP study. I could
run these commands to get them installed:

```bash
cd ExampleAnalysis
./code/install_rbc.py \
    --qc-threshold complete-pass \
    --release 1.0 \
    --bold-studies CCNP \
    --anat-studies CCNP
```

This will result in two new directories:
  * `inputs/data/CCNP_FreeSurfer`
  * `inputs/data/CCNP_CPAC`

You can `cd` into these directories to see what sort of data is
available. To access the content of any of the files in these directories
you will need to `datalad get` specific files.

**Do not attempt to download the entire datasets unless you want to run out of disk space**


### Running analysis scripts

In the `code/` directory you will find an example script that that performs
a couple steps:

  1) `datalad get` the tabular data that you want to analyze
  2) combines these data into a single tsv file
  3) calculates some stats on them

