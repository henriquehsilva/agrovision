# Lê exports/agrovision.csv e calcula média/desvio por cultura
# Uso: Rscript r/estatisticas.R

df <- read.csv("exports/agrovision.csv", stringsAsFactors = FALSE)
if (nrow(df) == 0) stop("CSV vazio. Exporte pelo CLI primeiro.")

agg <- aggregate(cbind(area_m2, area_ha) ~ cultura, df, function(x) c(mean=mean(x), sd=sd(x)))
print("=== Estatísticas por cultura ===")
print(agg)
