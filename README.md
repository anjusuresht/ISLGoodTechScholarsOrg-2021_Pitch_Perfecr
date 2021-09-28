# ISLGoodTechScholarsOrg-2021_Pitch_Perfecr
PITCH PERFECT: A platform, For ideas to reach its true potential

List of Personas:

 	Students / Developers (Founders)
 	Login / Sign In
 	Domain
	Idea submission (Create / Save / Delete)
	Validate idea
	List ideas with matching
	Accept / Reject invitation from investor
	Investors
	Login / Sign In
	Filter / Search ideas
	Rate / Comment on Ideas
	Interest (Partial interest for collaboration)
	Setup meeting
 	Invest
Database Schema:

![image](https://user-images.githubusercontent.com/83357771/135121514-376bf7ba-c259-4f95-bac5-37947041f306.png)

API’s needed:

  	Login API (v1/pitchperfect/login)
  	API for submit(v1/pitchperfect/idea)
  	API to retrieve project names and abstracts
  	API to retrieve projects based on filters / Search API
	  API to save project details
	  API to delete project details
	  API for investors to show interest in a project
	  API for investors to invest on projects

API	Methods	Response code	Input	Response Json/String
v1/pitchperfect/login	POST	200 
	User,password	Json with access token
		401		Unauthorized
		403		Forbidden
v1/pitchperfect/idea	POST	201	{"title":"","abstract":"","scope":"","implementationDetails":""}	Id, timestamp
v1/pitchperfect/idea/{id}	PUT	200	{"title":"","abstract":"","scope":"","implementationDetails":""}	
	DELETE	204		
	GET	200		Title,abstract,scope,implementation detail,timestamp(created),timestamp(updated)
v1/pitchperfect/idea/{id}/rate	POST	200		
	GET	200		Rating value
v1/pitchperfect/idea/{id}/comment	POST,GET,DELETE	200,200,200		Post-
Get-all the comments


