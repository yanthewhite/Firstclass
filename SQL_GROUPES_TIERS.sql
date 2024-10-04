SELECT
	UPPER(TRIM(
		SUBSTRING(TRIM(gcDesignation),
			LENGTH(TRIM(gcCompteGen)) + 1,
			(
				LENGTH(TRIM(gcDesignation)) - LENGTH(TRIM(gcCompteGen))
			)
		)
	))
	AS Designation_Groupe_Tiers,
	gcCompteGen AS Compte_General,
	(CASE gcExcluCA
		WHEN 0 THEN "NON"
		ELSE 'OUI'
	END) AS Exclus_CA
FROM tblgrouptiers
