import streamlit as st

# Define DevOps tools 
devops_tools = {
    "Plan": [
        {"name": "Jira"}, 
        {"name": "Trello"}, 
        {"name": "Asana"}, 
        {"name": "Monday.com"}, 
        {"name": "Confluence"}, 
        {"name": "GitHub"}, 
        {"name": "GitLab"}, 
        {"name": "Bitbucket"}, 
    ],
    "Code": [
        {"name": "Git"}, 
        {"name": "GitHub"}, 
        {"name": "GitLab"}, 
        {"name": "Bitbucket"}, 
        {"name": "GitKraken"}, 
        {"name": "Visual Studio Code"}, 
        {"name": "IntelliJ IDEA"}, 
        {"name": "PyCharm"}, 
        {"name": "Sublime Text"}, 
        {"name": "Vim"}, 
        {"name": "Atom"}, 
        {"name": "Markdown"}, 
        {"name": "Sphinx"}, 
        {"name": "Doxygen"}, 
        {"name": "TensorFlow"}, 
        {"name": "PyTorch"}, 
    ],
    "Build": [
        {"name": "Jenkins"}, 
        {"name": "Azure DevOps Pipelines"}, 
        {"name": "GitLab CI/CD"}, 
        {"name": "CircleCI"}, 
        {"name": "Bamboo"}, 
        {"name": "Maven"}, 
        {"name": "Gradle"}, 
        {"name": "Ant"}, 
        {"name": "Make"}, 
        {"name": "Docker"}, 
        {"name": "SonarQube"}, 
        {"name": "JFrog Artifactory"}, 
        {"name": "Nexus"}, 
    ],
    "Test": [
        {"name": "JUnit"}, 
        {"name": "pytest"}, 
        {"name": "NUnit"}, 
        {"name": "Selenium"}, 
        {"name": "Cypress"}, 
        {"name": "JMeter"}, 
        {"name": "Postman"}, 
        {"name": "SoapUI"}, 
        {"name": "SonarQube"}, 
        {"name": "Checkmarx"}, 
        {"name": "OWASP ZAP"}, 
        {"name": "Nessus"}, 
    ],
    "Deploy": [
        {"name": "Docker"}, 
        {"name": "Kubernetes"}, 
        {"name": "Docker Swarm"}, 
        {"name": "Terraform"}, 
        {"name": "Ansible"}, 
        {"name": "Puppet"}, 
        {"name": "Chef"}, 
        {"name": "SaltStack"}, 
        {"name": "AWS"}, 
        {"name": "Azure"}, 
        {"name": "GCP"}, 
        {"name": "Octopus Deploy"}, 
        {"name": "Spinnaker"}, 
        {"name": "Vault"}, 
    ],
    "Operate": [
        {"name": "Kubernetes"}, 
        {"name": "Docker Swarm"}, 
        {"name": "Terraform"}, 
        {"name": "Ansible"}, 
        {"name": "Puppet"}, 
        {"name": "Chef"}, 
        {"name": "SaltStack"}, 
        {"name": "AWS"}, 
        {"name": "Azure"}, 
        {"name": "GCP"}, 
        {"name": "Prometheus"}, 
        {"name": "Grafana"}, 
        {"name": "ELK Stack"}, 
        {"name": "Datadog"}, 
        {"name": "New Relic"}, 
        {"name": "Dynatrace"}, 
        {"name": "CloudWatch (AWS)"}, 
        {"name": "Azure Monitor"}, 
        {"name": "Cloud Monitoring (GCP)"}, 
        {"name": "Vault"}, 
        {"name": "MySQL"}, 
        {"name": "PostgreSQL"}, 
        {"name": "MongoDB"}, 
        {"name": "Redis"}, 
    ],
    "Monitor": [
        {"name": "Prometheus"}, 
        {"name": "Grafana"}, 
        {"name": "ELK Stack"}, 
        {"name": "Datadog"}, 
        {"name": "New Relic"}, 
        {"name": "Dynatrace"}, 
        {"name": "CloudWatch (AWS)"}, 
        {"name": "Azure Monitor"}, 
        {"name": "Cloud Monitoring (GCP)"}, 
    ],
    "All": [
        {"name": "Slack"}, 
        {"name": "Microsoft Teams"}, 
        {"name": "Hubot"}, 
        {"name": "Errbot"}, 
        {"name": "Flow"}, 
        {"name": "Plutora"}, 
    ]
}

# Create a Streamlit app
st.title("DevOps Tools by Phase")

# Create a dropdown for selecting the phase
selected_phase = st.selectbox("Select Phase:", list(devops_tools.keys()))

# Create a search bar
search_term = st.text_input("Search for tools")

# Filter tools based on search term
filtered_tools = [tool for tool in devops_tools[selected_phase] if search_term.lower() in tool["name"].lower()]

# Display the tools for the selected phase
st.write(f"**Tools for {selected_phase}:**")
for tool in filtered_tools:
    st.write(f"- {tool['name']}")