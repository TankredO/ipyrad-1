#!/usr/bin/env python

""" Return explanation and options for each parameter. 
    ip.get_params_info(1) or ip.get_params_info("project_dir") 
    return the same result. If not argument, a summary of the available
    parameters and their numbered references is returned. 
    Parameter info is stored as a dict of tuples. Each tuple consists of a
    short and a long desription for each parameter. By default if you as
    for a parameter you'll get the long description
"""

from __future__ import print_function
from collections import OrderedDict


pinfo = OrderedDict([
("0", ("""
    (0) assembly_name ----------------------------------------------------
    This is the name of your assembly. It will be the prefix for all 
    directories inside the project directory. An easy default for this
    parameter is the name of your project directory. For example if your
    project directory is ./white-crowns, then your assembly name could be
    white-crowns. Assembly name is variable because you might want to
    fork assemblies within a project to try different runs with different
    minimum coverage values, different levels of indels allowed, etc.
    Examples:
    ----------------------------------------------------------------------
    data.set_params('assembly_name', "white-crowns")     ## verbose
    ----------------------------------------------------------------------
    """, "Assembly name. Used to name output directories for assembly steps")
),
("1", ("""
    (1) project_dir ------------------------------------------------------
    Project name / path for working directory where all data files will be 
    saved. This parameter affects all steps of assembly (1-7). 
    Examples: 
    ----------------------------------------------------------------------
    data.set_params('project_dir', "./")                 ## verbose
    ----------------------------------------------------------------------
    """, "Project dir (made in curdir if not present)")
),

("2", ("""
    (2) raw_fastq_path ---------------------------------------------------
    The directory or files (selected with * wildcard selector) in which 
    FASTQ data files reside. Files can be gzipped. This parameter affects 
    only step 1 of assembly. Examples:
    ----------------------------------------------------------------------
    data.set_params("raw_fastq_path", "raw/*.fastq.gz")   ## verbose 
    ----------------------------------------------------------------------
    """, "Location of raw non-demultiplexed fastq files")
),

("3", ("""
    (3) barcodes_path ----------------------------------------------------
    Path to the barcodes file used in step 1 of assembly for 
    demultiplexing. If data are already demultiplexed this can be left 
    blank. This parameter affects only step 1 of assembly. NB: iPyrad
    can only handle one barcodes file at a time, so if you have multiple
    barcodes files and multiple raw files then you'll need to run each
    separately. Examples:
    ----------------------------------------------------------------------
    data.set_params("barcodes_path", "./barcodes.txt")    ## verbose
    ----------------------------------------------------------------------
    """, "Location of barcodes file")
),

("4", ("""
    (4) sorted_fastq_path ------------------------------------------------
    Path to demultiplexed fastq data. If left blank, this is assigned
    automatically to <data.name>_fastq/ within the working directory. If your
    data are already demultiplexed then you must enter the location of your  
    data here. Wildcard selectors can be used to select a subsample of files 
    within a directory, else all files are selected in the directory.
    This parameter affects only step 2 of assembly. 
    Examples:
    ----------------------------------------------------------------------
    data.set_params("sorted_fastq_path", "data/*.gz")     ## 
    ----------------------------------------------------------------------
    """, "Location of demultiplexed/sorted fastq files")
),

("5", ("""
    (5) assembly_method --------------------------------------------------
    A string specifying the desired assembly method. There are four 
    available options for assembly method:
           denovo -   Denovo assembly is the classic pyrad method, and
                      it is the <default> unless otherwise specified.
                      Denovo will cluster and align all reads from scratch
        reference -   Reference assembly will map and align reads to the
                      provided reference sequence, which must be specified
                      in parameter 28 (reference_sequence). Strict refer-
                      ence assembly will throw out all unmapped reads, 
                      which could be a significant proportion depending
                      on the distance between your reference and study
                      species.'.
     ----------------------------------------------------------------------
    data.set_params("assembly_method", "denovo")   ## verbose
    ---------------------------------------------------------------------- 
    """, "Assembly method (denovo, reference)")
),

("6", ("""
    (6) reference_sequence -----------------------------------------------
    The path to the reference sequence you desire to map your reads to.
    The reference may be either fasta or gzipped fasta. It should be a 
    complete reference sequence, including all chromosomes, scaffolds, and
    contigs in one huge file (most reference sequences available will be
    in this format, especially non-model references). The first time you 
    attempt to use this sequence it will be indexed (we are using bwa
    for reference mapping). This is a time intensive process so expect the 
    first run to take some time, certainly more than ten minutes, but less 
    than an hour. If you desire to index the reference yourself you can do 
    this, but best not to unless you really care about bwa indexing 
    settings. We chose conservative defaults that have worked well for us 
    on other projects. 

    A word on the format of the path (this is important). The path may
    either be a full path (desirable) or a path relative to the directory
    you are running ipyrad from (supported but be careful of the path).
    ----------------------------------------------------------------------
    data.set_params(6) = /home/wat/data/reference.fa  ## set a full path
    data.set_params(6) = ./data/reference.fa.gz       ## set a relative path
    data.set_params("reference_sequence") = ./data/reference.fa   ## verbose
    ---------------------------------------------------------------------- 
    """, "Location of reference sequence file")
),

("7", ("""
    (7) datatype ---------------------------------------------------------
    Options: rad, gbs, 2brad, ddrad, pairddrad, pairgbs, pair3rad,
    This parameter affects all steps of assembly (1-7).         
    Examples:
    ----------------------------------------------------------------------
    data.set_params(7) = 'rad'                     ## rad data type
    data.set_params(7) = 'gbs'                     ## gbs data type
    data.set_params(7) = 'pairddrad'               ## gbs data type        
    data.set_params("datatype") = 'ddrad'          ## verbose
    ----------------------------------------------------------------------
    """, "Datatype (see docs): rad, gbs, ddrad, etc.")
),

("8", ("""
    (8) restriction_overhang ---------------------------------------------
    A tuple containing one or two restriction overhangs. Single digest 
    RADseq with sonication requires only one overhange, all other data 
    types should have two. The first is used for detecting barcodes, the 
    second is not required, but is used in filtering, and is needed for 
    removal from short DNA fragments. This parameter affects steps 1,2,4,5, 
    and 7 of assembly. 
    Examples:
    ----------------------------------------------------------------------
    data.set_params(8) = ("TGCAG", "")           ## default rad (PstI)
    data.set_params(8) = ("CWGC", "CWGC")        ## gbs or pairgbs (ApeKI)
    data.set_params(8) = ("CAGT", "AATT")        ## ddrad (ApeKI, MSI)
    data.set_params(8) = ("CAGT", "AATT")        ## pairddrad (ApeKI, MSI)        
    data.set_params("restriction_overhang") = ("CAGT", "AATT")   ## verbose
    ----------------------------------------------------------------------
    """, "Restriction overhang (cut1,) or (cut1, cut2)")
),

("9", ("""
    (9) max_low_qual_bases -----------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(9) = 10
    data.set_params("max_low_qual_bases") = 6
    ----------------------------------------------------------------------
    """, "Max low quality base calls (Q<20) in a read")
),

("10", ("""
    (10) phred_Qscore_offset ---------------------------------------------
    The threshold at which a base call is considered low quality during 
    step 2 filtering is determined by the phred_Qscore_offset. The default
    offset is 33, which is equivalent to a minimum qscore of 20 (99% call
    confidence). Some older data use a qscore offset of 64. You can toggle 
    the offset number to change the threshold for low qual bases. For 
    example, reducing the offset to 26 is equivalent to a minimum qscore 
    of 13, which is approximately 95% probability of a correct base call.

    Examples:
    ----------------------------------------------------------------------
    data.set_params(10) = 33
    data.set_params("phred_Qscore_offset") = 26     ## 95% confidence
    data.set_params("phred_Qscore_offset") = 43     ## 99.9% confidence
    data.set_params("phred_Qscore_offset") = 33
    ----------------------------------------------------------------------
    """, "phred Q score offset (33 is default and very standard)")
),

("11", ("""
    (11) mindepth_statistical --------------------------------------------
    An integer value indicating the mindepth for statistical base calls
    based a binomial probability with H and E estimated from the data.
    Base calls are made at >= the value entered. For most reasonable 
    estimates of E and H, statistical base calls cannot be made below 5 
    or 6, and will instead be called N. 
    The parameter affects steps 5 and 7 of assembly. 
    Examples:
    ----------------------------------------------------------------------
    data.set_params(11) = (6, 6)    ## only stat base calls down to depth=6
    data.set_params(11) = (10, 5)   ## stat calls above 9, majrule from 9-5.
    data.set_params(11) = (10, 1)   ## stat calls above 9, majrule from 9-1.
    data.set_params(mindepth_statistical) = 6    ## verbose
    ----------------------------------------------------------------------
    """, "Min depth for statistical base calling")
),

("12", ("""
    (12) mindepth_majrule ------------------------------------------------
    An integer value indicating the mindepth for majority-rule base calls. 
    Base calls are made at >= the value entered. It may often be advant-
    ageous to use a low value for majrule calls to preserve most data during 
    assembly within-samples, so that more data is clustered between samples. 
    Low depth data can be filtered out later from the final data set if needed. 
    The parameter affects steps 5 and 7 of assembly. 
    Examples:
    ----------------------------------------------------------------------
    data.set_params(12) = (6, 6)    ## only stat base calls down to depth=6
    data.set_params(12) = (10, 5)   ## stat calls above 9, majrule from 9-5.
    data.set_params(12) = (10, 1)   ## stat calls above 9, majrule from 9-1.
    data.set_params(mindepth_majrule) = 6    ## verbose
    ----------------------------------------------------------------------
    """, "Min depth for majority-rule base calling")
),

("13", ("""
    (13) maxdepth --------------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(13) = 33
    data.set_params("maxdepth") = 33
    ----------------------------------------------------------------------
    """, "Max cluster depth within samples")
),

("14", ("""
    (14) clust_threshold -------------------------------------------------
    Clustering threshold. 
    Examples:
    ----------------------------------------------------------------------
    data.set_params(14) = .85          ## clustering similarity threshold
    data.set_params(14) = .90          ## clustering similarity threshold
    data.set_params(14) = .95          ## very high values not recommended 
    data.set_params("clust_threshold") = .83  ## verbose
    ----------------------------------------------------------------------
    """, "Clustering threshold for de novo assembly")
),

("15", ("""
    (15) max_barcode_mismatch --------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(15) = 1
    data.set_params("max_barcode_mismatch") = 1
    ----------------------------------------------------------------------
    """, "Max number of allowable mismatches in barcodes")
),

("16", ("""
    (16) filter_adapters ----------------------------------------------
    Examples:
    -------------------------------------------------------------------
    data.set_params(16) = 1
    data.set_params("filter_adapters") = 1
    -------------------------------------------------------------------
    """, "Filter for adapters/primers (1 or 2=stricter)")
),

("17", ("""
    (17) filter_min_trim_len ---------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(17) = 1
    data.set_params("filter_min_trim_len") = 1
    ----------------------------------------------------------------------
    """, "Min length of reads after adapter trim")
),

("18", ("""
    (18) max_alleles_consens ---------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(18) = 1
    data.set_params("max_alleles_consens") = 1
    ----------------------------------------------------------------------
    """, "Max alleles per site in consensus sequences")
),

("19", ("""
    (19) max_Ns_consens --------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(19) = 1
    data.set_params("max_Ns_consens") = 1
    ----------------------------------------------------------------------
    """, "Max N's (uncalled bases) in consensus")
),

("20", ("""
    (20) max_Hs_consens --------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(20) = 1
    data.set_params("max_Hs_consens") = 1
    ----------------------------------------------------------------------
    """, "Max Hs (heterozygotes) in consensus")
),

("21", ("""
    (21) min_samples_locus -----------------------------------------------
    Minimum number of samples a locus must be shared across to be included
    in the exported data set following filtering for sequencing depth, 
    paralogs, ...
    Examples
    ----------------------------------------------------------------------
    data.set_params(21) = 4            ## min 4; most inclusive phylo data 
    data.set_params(21) = 20           ## min 20; less data, less missing
    data.set_params(21) = 1            ## min 1; most data, most missing
    data.set_params("min_samples_locus") = 4     ## verbose
    ----------------------------------------------------------------------
    """, "Min # samples per locus for output")
),

("22", ("""
    (22) max_SNPs_locus --------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(22) = 1
    data.set_params("max_SNPs_locus") = 1
    ----------------------------------------------------------------------
    """, "Max # SNPs per locus")
),

("23", ("""
    (23) max_Indels_locus ------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params(23) = 1
    data.set_params("max_Indels_locus") = 1
    ----------------------------------------------------------------------
    """, "Max # of indels per locus")
),

("24", ("""
    (24) max_shared_Hs_locus ---------------------------------------------
    ...
    ----------------------------------------------------------------------
    data.set_params(24) = .25          ## set as proportion of samples
    data.set_params(24) = 4            ## set as number of samples
    data.set_params(24) = 9999         ## set arbitrarily high
    data.set_params("max_shared_Hs_locus") = 4      ## verbose
    ----------------------------------------------------------------------
    """, "Max # heterozygous sites per locus")
),

("25", ("""
    (25) trim_reads -- ---------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params("trim_reads") = (0, -5, 0, 0)  ## trims last 5 from R1
    data.set_params("trim_reads") = (5, 85, 0, 0)  ## trims R1 from 5-85
    data.set_params("trim_reads") = (5, 85, 5, 85) ## trims both pairs 5-85
    ----------------------------------------------------------------------
    """, "Trim raw read edges (R1>, <R1, R2>, <R2) (see docs)")
),

("26", ("""
    (26) trim_loci -------------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params("trim_loci") = (0, 5, 5, 0)
    ----------------------------------------------------------------------
    """, "Trim locus edges (see docs) (R1>, <R1, R2>, <R2)")
),

("27", ("""
    (27) output_formats --------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    *                      ## [27] output_formats: * means all formats
    vcf, phy, nex          ## [27] list subset of formats if you want
    ----------------------------------------------------------------------
    """, "Output formats (see docs)")
),

("28", ("""
    (28) pop_assign_file -------------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    ./popfile.txt                               ## [28] pop_assign_file
    /home/users/Documents/popfile.txt           ## [28] pop_assign_file 
    ----------------------------------------------------------------------
    """, "Path to population assignment file")
),

("29", ("""
    (29) reference_as_filter ---------------------------------------------
    Examples:
    ----------------------------------------------------------------------
    data.set_params("reference_as_filter") = ./data/reference.fa   ## verbose
    ----------------------------------------------------------------------
    """, "Reads mapped to this reference are removed in step 3")
),

])

def paramname(param=""):
    """ Get the param name from the dict index value.
    """

    try: 
        name = pinfo[str(param)][0].strip().split(" ")[1]
    except (KeyError, ValueError) as err:
        ## TODO: paramsinfo get description by param string not working.
        ## It would be cool to have an assembly object bcz then you could
        ## just do this:
        ##
        ## print(pinfo[data.paramsinfo.keys().index(param)])
        print("\tKey name/number not recognized - ".format(param), err)
        raise

    return name


def paraminfo(param="", short=False):
    """ Returns detailed information for the numbered parameter. 
        Further information is available in the tutorial.
        Unlike params() this function doesn't deal well with *
        It only takes one parameter at a time and returns the desc
    """

    ## If the short flag is set return the short description, otherwise
    ## return the long.
    if short:
        desc = 1
    else:
        desc = 0

    try: 
        description = pinfo[str(param)][desc]
    except (KeyError, ValueError) as err:
        ## TODO: paramsinfo get description by param string not working.
        ## It would be cool to have an assembly object bcz then you could
        ## just do this:
        ##
        ## print(pinfo[data.paramsinfo.keys().index(param)])
        print("\tKey name/number not recognized - ".format(param), err)
        raise

    return description


def paramsinfo(param="", short=False):
    """ This is the human readable version of the paramsinfo() function.
        You give it a param and it prints to stdout.
    """
    if short:
        desc = 1
    else:
        desc = 0

    if param == "*":
        for key in pinfo:
            print(pinfo[str(key)][desc])
    elif param:
        try:
            print(pinfo[str(param)][desc])
        except (KeyError, ValueError) as err:
            ## TODO: paramsinfo get description by param string not working.
            ## It would be cool to have an assembly object bcz then you could
            ## just do this:
            ##
            ## print(pinfo[data.paramsinfo.keys().index(param)])
            print("\tKey name/number not recognized", err)
            raise
    else:
        print("Enter a name or number for explanation of the parameter\n")
        for key in pinfo:
            print(pinfo[str(key)][desc].split("\n")[1][2:-10])


if __name__ == "__main__":
    pass
