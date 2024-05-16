﻿# Job_Id_LinkdIn_Scrapper-
Here are the requirements by client for this scrapper.

What you should extract:
→ Job ID,
→ Job Title,
→ Company Name,
→ Location,
→ Job Type,
→ Job Description (With innerHTML),
→ Apply URL.

The script needs to:
→ Be prepared for using proxies,
→ Handle all errors (404, 429, etc),
→ Be able to choose how much pagination we want to extract,
→ Decode the Apply URL,
→ Save to a CSV with column headers (job.id, job.title),
→ Be able to stop the script and save all the data extracted to that time (for example if PC shutdown).

** About Location **

You need to use a function like this:

locations = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setubal", "Viana do Castelo", "Vila Real", "Viseu", "Açores", "Madeira"]
def extract_district(location):
for district in locations:
if district.lower() in location.lower():
return district
return None

To extract only the District from location.

Some data you will need:
→ Url paginations: https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?&geoId=100364837&f_TPR=r604800&f_WT=1&start=
→ Job post: https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/

