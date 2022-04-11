import streamlit as st
import streamlit.components.v1 as components


def main():
	st.title("""Chicago Facility Health Inspections""")
	st.write("""CDC estimates that each year roughly 1 in 6 Americans (or 48 million people) gets sick, 128,000 are hospitalized, and 3,000 die of foodborne diseases. People should feel comfortable going to a food distributing facility knowing they have successfully passed their inspections. 

""")
	html_temp = """
<div class='tableauPlaceholder' id='viz1649615686813' style='position: relative'><noscript><a href='#'><img alt='Top Inspection Fail Types ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book5_16496156724630&#47;TopInspectionFailTypes&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book5_16496156724630&#47;TopInspectionFailTypes' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book5_16496156724630&#47;TopInspectionFailTypes&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1649615686813');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
		"""
	components.html(html_temp, height =700, width= 1000)
	st.write("""An inspection can be one of the following types:""")
	st.write(""" * Canvass: The most common type of inspection performed at a frequency relative to the risk of the establishment""")
	st.write(""" * Consultation: when the inspection is done at the request of the owner prior to the opening of the establishment""")
	st.write(""" * Complaint: when the inspection is done in response to a complaint against the establishment; license, when the inspection is done As a requirement for the establishment to receive its license to operate""")
	st.write(""" * Suspect food poisoning: when the inspection is done in response to one or more persons claiming to have gotten ill as a result of eating at the establishment""") 
	st.write(""" * Task-force inspection: when an inspection of a bar or tavern is done""")
	st.write(""" * Re-inspections can occur for most types of these inspections and are indicated as such. """)
	html_temp2 = """
		<div class='tableauPlaceholder' id='viz1649613369610' style='position: relative'><noscript><a href='#'><img alt='60622 Zipcode Fail Facilities Grouped ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;KJ&#47;KJC2HZHT6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;KJC2HZHT6' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;KJ&#47;KJC2HZHT6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1649613369610');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script> 
		"""
	components.html(html_temp2, height = 500, width= 1130)
	st.write("""View all Facilities that failed in Chicago in 2022""")
	html_temp3 = """
		<div class='tableauPlaceholder' id='viz1649618422920' style='position: relative'><noscript><a href='#'><img alt='2022 Resturant Fail by Zipcode ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;FJ&#47;FJZSC2WQ6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;FJZSC2WQ6' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;FJ&#47;FJZSC2WQ6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1649618422920');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
		"""
	components.html(html_temp3, height = 500, width= 1130)
	

	html_temp5 = """
		<div class='tableauPlaceholder' id='viz1649619250417' style='position: relative'><noscript><a href='#'><img alt='Average Fail by Facility Group ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book8_16496192074730&#47;AverageFailbyFacilityGroup&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book8_16496192074730&#47;AverageFailbyFacilityGroup' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book8_16496192074730&#47;AverageFailbyFacilityGroup&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1649619250417');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
		"""
	components.html(html_temp5, height = 500, width= 1130)
    
    
if __name__ == "__main__":    
    main()
    
    
    
    
