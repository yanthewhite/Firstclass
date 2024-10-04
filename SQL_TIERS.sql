SELECT
	TRIM(UPPER(ttDesignation)) AS Type_Tiers, 
	cpCode AS Num_Compte, 
	TRIM(UPPER(cpRaisonSocial)) AS intitule, 
	cpCptGenPrinc AS Num_Compte_General,
	TRIM(UPPER(cgDesignation)) AS Categorie_Comptables,
	TRIM(UPPER(cpPays)) AS Pays,  	
	TRIM(UPPER(cpVille)) AS Ville, 
	IF(((cpTel1 IS NOT NULL) OR (TRIM(cpTel1) <> "")),cpTel1,
	  IF(((cpTel2 IS NOT NULL) OR (TRIM(cpTel2) <> "")), cpTel2,0
	  )
	)AS Num_Tel,
	TRIM(UPPER(cpBP)) AS BP, 
	TRIM(UPPER(cpTelex)) AS Telex, 
	TRIM(UPPER(cpFax)) AS FAX, 
	TRIM(cpEmail) AS E_Mail

FROM tblcomptes cpttiers
	LEFT OUTER JOIN tblcategorietiers categtiers
	ON cpttiers.cgIdent = categtiers.cgIdent
	LEFT OUTER JOIN messa2015.tbltypetiers typetiers
	ON cpttiers.ttIdent = typetiers.ttIdent 
ORDER BY ttDesignation
