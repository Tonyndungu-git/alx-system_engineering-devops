# WordPress Website Outage Postmortem

<div align="center">
  <img src="https://drive.google.com/uc?id=1bmWPGvJj0myr0LautviTXONzwXQZshFO" alt="Outage Fun Image" width="400px" />
</div>


## **Issue Summary**

- **Duration:** August 10, 2023, 10:00 AM to August 10, 2023, 2:00 PM (EAT)
- **Impact:** Complete service disruption of WordPress website hosted on LAMP stack, resulting in a 100% outage.
- **Root Cause:** Misconfigured Apache virtual host leading to a 500 Internal Server Error.

## **Timeline**

- **10:00 AM:** Monitoring tools detect a surge in HTTP 500 error responses.
- **10:15 AM:** DevOps team escalates the incident due to high error rates.
- **10:30 AM:** Initial investigation begins, focusing on logs and metrics. Assumption: Sudden traffic increase.
- **11:00 AM:** Apache error logs reveal mod_rewrite issues and virtual host misconfiguration.
- **11:30 AM:** Misleading investigation suspects DDoS attack, ruled out by traffic analysis.
- **12:00 PM:** Systems team takes over, identifies misconfigured virtual host as root cause.
- **1:00 PM:** Virtual host configuration is corrected, Apache service restarted, website resumes normal operation.
- **2:00 PM:** Issue resolved.

## **Root Cause and Resolution**

The root cause was a misconfigured virtual host file for Apache. The lack of mod_rewrite directives resulted in URL rewriting failure, generating 500 Internal Server Errors. The Systems team resolved the issue by updating the virtual host configuration with correct mod_rewrite directives and rules.

## **Corrective and Preventative Measures**

1. **Configuration Audits:** Regular audits of server configurations to identify misconfigurations.
2. **Automated Testing:** Implement automated tests for critical functionalities after configuration changes.
3. **Enhanced Monitoring:** Strengthen monitoring for specific HTTP error codes.
4. **Documentation Updates:** Maintain up-to-date server configuration documentation.
5. **Incident Response Plan:** Enhance response plan with clear escalation paths and responsibilities.
6. **Training:** Conduct training sessions to share incident lessons and improve troubleshooting skills.
7. **Backup and Rollback:** Implement rollback strategy for configuration-related issues.

Remember, even in the darkest bits and bytes, a little humor and a dash of creativity can turn a technical tale into an unforgettable adventure. Until next time, stay curious and keep those servers groovin'!!