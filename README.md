# 🏢 RVX ONE — Plateforme Globale de Gestion des Opérations et Maintenance
> **Powered by RELVORIX SERVICES**  
> *Une architecture logicielle centralisée, sécurisée (Zero-Trust) et automatisée pour le Facility Management 4.0.*

---

## 📌 1. Présentation du Projet
**RVX ONE** est une solution numérique d'entreprise conçue exclusivement pour centraliser, coordonner, piloter et suivre l'intégralité des prestations de services et interventions techniques gérées par **RELVORIX SERVICES**. 

Elle élimine définitivement la dispersion des données (Excel, WhatsApp, rapports papier) et assure une traçabilité totale en temps réel.

### 🎯 Périmètre de Gestion (21 Modules Intégrés) :
* **Entités Fondamentales :** Gestion des Clients, Gestion des Sites/Infrastructures, Gestion des Contrats et Documents.
* **Flux Opérationnels :** Demandes de Services (Helpdesk), Suivi des Interventions, Planning et Calendrier Dynamique.
* **Maintenance Technique :** Maintenance Préventive Calculée, Maintenance Corrective Intégrée, Fiches de Contrôle Qualité.
* **Gestion Financière :** Pilotage des Devis techniques (RVX Quote), Suivi strict des Coûts (Fournisseurs vs Marges).
* **Intelligence Métier :** Analyse de Récurrence des Pannes, Suivi en temps réel des Indicateurs de Performance (KPIs), Rapports et Historiques.

---

## 🔒 2. Architecture Sécuritaire & Isolation (Zero-Trust)
Le framework intègre nativement des protocoles de sécurité avancés pour protéger l'intégrité des données des entreprises clientes :

* **Sécurisation contre les failles IDOR & Injections :** Protection stricte au niveau du serveur pour interdire la manipulation des paramètres URL.
* **Isolation stricte des Prestataires (Data Isolation) :** Le prestataire A n'a aucun accès aux données, sites ou tickets du prestataire B.
* **Gestion des Rôles (RBAC Matrix) :**
  * `Relvorix Admin` : Contrôle global et supervision financière.
  * `Quality Controller` : Validation des fiches de contrôle avant clôture.
  * `Technician` : Accès terrain mobile restreint aux tâches assignées.
  * `Client` : Visibilité exclusive sur ses propres infrastructures et statuts.

---

## 📲 3. Fonctionnalités Terrain & Automatisation

### 🔲 Génération Automatique de QR Codes :
Chaque équipement (Pompes, Climatiseurs, Armoires Électriques) reçoit un identifiant unique dès son insertion. Le script backend génère automatiquement un **QR Code chiffré**. Le technicien doit obligatoirement scanner ce QR Code sur site pour ouvrir sa fiche d'intervention (Preuve de Présence Physique).

### 🔄 Cycle de Vie des Demandes (Workflow en 11 Étapes) :
Les tickets suivent un parcours ultra-précis pour garantir le respect des délais :
`NEW` ➡️ `QUALIFIED` ➡️ `ASSIGNED` ➡️ `QUOTE REQUIRED` ➡️ `WAITING CLIENT APPROVAL` ➡️ `SCHEDULED` ➡️ `IN PROGRESS` ➡️ `WAITING CONTROL` ➡️ `CONTROLLED` ➡️ `COMPLETED` ➡️ `CLOSED`

### ✍️ Clôture Sécurisée par Signature Digitale :
Un ticket ne peut jamais passer à l'état final `CLOSED` sans l'intégration de la signature tactile du client sur l'application mobile et la validation de la **Checklist Qualité (OK / NOK)** par le superviseur.

---

## 📈 4. Tableaux de Bord & KPIs (Manager View)
L'interface d'administration offre une visibilité instantanée sur la santé opérationnelle de l'entreprise :
* **Alertes SLA :** Notification visuelle immédiate en cas de dépassement du délai de résolution contractuel de **4 heures**.
* **Générateur de Rapports :** Exportation en 1-clic des données opérationnelles sous formats **PDF récapitulatif** et **Excel/CSV** pour les analyses comptables.
* **Analyse de Récurrence :** Algorithme détectant automatiquement les équipements à forte fréquence de panne pour optimiser le parc matériel.

---

## 🛠️ 5. Structure Technique du Dépôt
* `/rvx_one` : Cœur de l'application (Frappe App Framework).
* `/rvx_one/security/rules.py` : Matrice de sécurité, rôles et workflow.
* `/files/rvx_ticket.py` : Logique serveur de calcul des SLAs et validation des signatures.
* `/files/rvx_equipment.py` : Script serveur de génération automatique des QR Codes.
* `/files/install.py` : Script d'automatisation des tables et schémas SQL.

---
© 2026 **RELVORIX SERVICES**. All Rights Reserved. Product Architecture Blueprint.
