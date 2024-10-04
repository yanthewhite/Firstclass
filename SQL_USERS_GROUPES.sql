SELECT
  UPPER(TRIM(grNom)) AS Users_Groupe_Code,
  UPPER(TRIM(grDescription)) AS Users_Groupe_Designations
FROM tblgroupe
