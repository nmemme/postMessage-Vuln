Exploiting postMessage() Vulnerabilities
===========================================

Team 4 
* Nicholas "Master Sorcerer" Memme
* Damilola "Crash Dust" Orikogbo 
* Tarana "Tweaked Geek" Chowdhury
* Carrie "Corrupt Geek" Cramer
* Zachery "Electric Goon" Sarkis
* Maria "Maximum Scorpion" Kromis

As web-based technology grows and expands, it is necessary for the security restrictions to adapt and expand in tandem. Therefore, while the Same Origin Policy, the center of web-based security, still holds an important place in web-security, it has proven that addendums are required. The Same Origin Policy, has held such a vital place in web-security, because it enforced the extremely vital function, of prohibiting users from either requesting data or information from another site if they do not come from the same protocol, port, and host. Which effectively prevents an entire subset of malicious attacks in a single swoop. In the beginnings of web security, when most hosts were stand alone, and most outside information requests were from malicious attackers, this policy’s steadfast restrictions were beneficial. However, now as the format and technology of websites change, and many hosts often integrate social media or user tailored advertisements into their sites, it is “often convenient or even necessary for frames from different origins to communicate with each other”[1]. Therefore, the restrictive SOP ban on cross-domain communication was necessary to be lifted, giving birth to the HTML5 post-messaging system.The postMessage() method was created to enable cross-document messaging between applications on the same hosting page, but that may not share the same port, host or protocol. This provides a vital service to modern websites that hosts different social media, or advertising domains on their site, While this was the original intention of the feature, if not appropriately protected against, this helpful feature can instead pose as a huge security risk. In fact, a malicious programmer could see this as almost a way around the same origin policy, and an opportunity to exploit attacks on the message receiver.
