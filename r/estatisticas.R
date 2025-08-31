# Lê exports/agrovision.csv e calcula média/desvio por cultura
# Uso: Rscript r/estatisticas.R

csv <- "exports/agrovision.csv"
if (!file.exists(csv)) {
  stop("CSV não encontrado. Exporte pelo menu da CLI: 'Exportar CSV' -> exports/agrovision.csv")
}
df <- read.csv(csv, stringsAsFactors = FALSE)
if (nrow(df) == 0) {
  stop("CSV está vazio. Cadastre dados e exporte novamente.")
}
agg <- aggregate(cbind(area_m2, area_ha) ~ cultura, df,
                 function(x) c(mean = mean(x), sd = sd(x)))
print("=== Estatísticas por cultura ===")
print(agg)
