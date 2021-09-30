# ISLGoodTechScholarsOrg-2021_Pitch_Perfect
PITCH PERFECT: A platform, For ideas to reach its true potential

List of Personas:

Students / Developers (Founders)
- Login / Sign In
- Domain
- Idea submission (Create / Save / Delete)
- Validate idea
- List ideas with matching
- Accept / Reject invitation from investor

Investors
- Login / Sign In
- Filter / Search ideas
- Rate / Comment on Ideas
- Interest (Partial interest for collaboration)
- Setup meeting
- Invest

Database:
Data is stored using MySQL

Database Schema:
![Untitled Diagram (1)](https://user-images.githubusercontent.com/83357771/135520657-2fc65e62-a647-46fd-a4f2-9c8ccf617a3b.jpg)


API’s needed:

- Login API (v1/pitchperfect/login)
- API for submit(v1/pitchperfect/idea)
- API to retrieve project names and abstracts
- API to retrieve projects based on filters / Search API
- API to save project details
- API to delete project details
- API for investors to show interest in a project
- API for investors to invest on projects

- [ ] Come up with DB schema - P0
- [ ] Database layer - to run queries / put data in DB - P0
- [ ] state diagram - **e.g** idea - drafted(future scope), saved, published, deleted **e.g** user - active
- [ ] v1/pitchperfect/login - P2
- [x] v1/pitchperfect/{userid}/idea POST, PUT, GET, DELETE - P1
- [x] v1/pitchperfect/idea	POST, PUT, GET - P1
- [x] v1/pitchperfect/idea/{id} GET  - P1
- [ ] v1/pitchperfect/{userid}/idea/{id}/asset  POST, PUT, GET, DELETE - P3
- [ ] v1/pitchperfect/idea/{id}/rate POST, GET - P3
- [ ] v1/pitchperfect/idea/{id}/comment POST, GET, PUT, DELETE - P3
- [ ] v1/pitchperfect/idea/{id}/interest POST, GET, DELETE - P3
- [ ] v1/pitchperfect/{userid}/idea/interest GET - P3
- [ ] v1/pitchperfect/idea/{id}/collaborate POST, GET, DELETE - P4
- [ ] Encyrpt database content - P4
- [ ] Package application - P3
- [ ] Containerize application - P3
- [ ] Deployment of application - P3

| API	                           | Methods	    | Response code	     | Input	                         | Response Json/String |
| -------------------------------- |-----------------| ----------------- | ----------------------------------|---------------------------|
| v1/pitchperfect/login	           |  POST	         | 200                | User,password|	                         Json with access token|
| 		                 |                   |     401		  |               |                             Unauthorized|
|		                 |                   |    403		   |               |                            Forbidden|				
| v1/pitchperfect/{userid}/idea  | POST | 201 | input json (field for copyrights) |  |
|                                | PUT | 200 | | |
|                                |   GET  | 200    | | |
|                                | DELETE | 204 | | |
| v1/pitchperfect/idea	         | POST	     | 201	|   {"title":"", "abstract":"", "scope":"","implementationDetails":""}|    	    Id, timestamp |
| v1/pitchperfect/{userid}/idea/{id}/asset | POST | 201 | input - file (supported file format) | | |
| v1/pitchperfect/{userid}/idea/{id}/asset | GET | 201 |  |  json response with asset list |
| v1/pitchperfect/{userid}/idea/{id}/asset/{assetId} | DELETE | 204 |  | | |
| v1/pitchperfect/{userid}/idea/{id}/asset/{assetId} | PUT | 201 |  | | |
| v1/pitchperfect/idea/{id}	  |    PUT	      |  200	|{"title":"", "abstract":"", "scope":"", "implementationDetails":""} | |	                                                               
|	                          |   DELETE	      |  204	 |	
|	                          |    GET	      |  200	 |	                    | Title,abstract,scope,implementation detail, timestamp(created),timestamp(updated) |                                                                                                                                                                                 
| v1/pitchperfect/idea/{id}/rate  |	POST	      | 200	 |                          |	
|	                          |    GET	      | 200	 |	                    |                         Rating value |
| v1/pitchperfect/idea/{id}/comment| POST|  200 |                        |  |
|  | GET | 200 | | Get-all the comments|
| | DELETE | 200 | |



Flow diagram:

![image](https://user-images.githubusercontent.com/83357771/135160213-b86460bf-7ff5-44d0-a7e9-8d48011993e5.png)



