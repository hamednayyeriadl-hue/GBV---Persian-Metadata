GBV – Persian Metadata (Göttingen University Library)
This repository contains a cleaned and structured dataset of approximately 100 Persian-language bibliographic records from the Göttingen University Library (GBV system).
The project focuses on transforming raw metadata into a usable, research-friendly format and documenting the data cleaning workflow.

Project Goals
-	Convert raw GBV metadata into structured CSV format
-	Discover and improve data consistency and usability as much as possible
-	Prepare the dataset for digital humanities and library research applications

Tools
-	Python for parsing and extracting raw metadata
-	OpenRefine for data cleaning, normalization, and reconciliation
-	Wikidata for entity reconciliation for personal names

Data Processing Workflow
1. Python Processing
-	Parsed raw metadata file
-	Identified fields based on fixed character position
-	Detected record boundaries using four consecutive blank lines
-	Preserved repeated fields using | as a separator
-	Exported structured CSV file (98 records)

2. OpenRefine Cleaning
-	Created Main Title for records with only collective titles
-	Extracted Primary Person (first individual listed)
-	Added Primary Person Role
-	Cleaned birth/death dates from name fields
-	Merged Author and Other Persons into a unified structure (Persons)
-	Reconciled Primary Person with Wikidata: 
o	32 matched entities
o	66 unmatched (likely lesser-known or modern authors)
•	Added Wikidata QIDs for matched entities

 
Metadata Challenges
The dataset reflects several common issues in legacy library metadata that should be considered:
-	Mixed Persian and Latin scripts within single fields
-	Author names embedded in title fields
-	Missing primary authors in some records (e.g., classical works)
-	Parallel and redundant columns (e.g., Author vs. Persons)
-	Inconsistent date formats (with/without special characters like *)
-	Inconsistent and wrong transliterations
-	Inappropriate information (like providing the publication turn as Edition)
-	Duplicate fields (e.g., Note vs. Notes)
-	Collective titles used instead of main titles
-	Roles recorded only in German (e.g., VerfasserIn, HerausgeberIn)
-	Empty values not consistently detected in OpenRefine (isBlank issue)

Dataset Overview
-	Total records: 98
-	Language: Persian (with multilingual metadata)
-	Source: GBV (Göttingen University Library)

Files
-	gbv-clean-txt.csv – cleaned dataset
-	Scripts
-	OpenRefine project

Future Work
-	Improve name authority control
-	Enhance reconciliation with Wikidata and VIAF
-	Normalize date formats
-	Separate multilingual fields
-	Publish as linked open data

Contributions
Suggestions, corrections, and collaborations are welcome—especially in the areas of metadata standards and Persian digital humanities.
