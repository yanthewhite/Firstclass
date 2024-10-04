SELECT
	TRIM(UPPER(ssfam.faCode)) AS Code_Familles,
	TRIM(UPPER(faDesignation)) AS Designation_Famille,
	TRIM(UPPER(sfCode)) AS Code_Sous_Familles,
	TRIM(UPPER(sfDesignation)) AS Designation_Sous_Famille,
	(CASE sfSuiviStock
		WHEN 0 THEN "NON"
		ELSE 'OUI'
	END) AS Suivi_Stock,
	TRIM(UPPER(sfNumCptGen)) AS Num_Compte_General
FROM tblsousfamille ssfam
	INNER JOIN tblfamille fam
	ON ssfam.faCode = fam.faCode
WHERE TRIM(UPPER(fam.faDesignation)) NOT LIKE "XX%" AND
TRIM(UPPER(fam.faDesignation)) NOT LIKE "%A CREER%" AND
TRIM(UPPER(ssfam.sfDesignation)) NOT LIKE "XX%" AND
TRIM(UPPER(ssfam.sfDesignation)) NOT LIKE "%A CREER%"
ORDER BY ssfam.faCode
