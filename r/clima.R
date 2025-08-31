# Coleta clima via Open-Meteo (sem chave), imprime resumo simples.
# Uso: Rscript r/clima.R -23.55 -46.63

args <- commandArgs(trailingOnly = TRUE)
lat <- ifelse(length(args)>=1, as.numeric(args[1]), -23.55)
lon <- ifelse(length(args)>=2, as.numeric(args[2]), -46.63)

url <- sprintf("https://api.open-meteo.com/v1/forecast?latitude=%f&longitude=%f&hourly=temperature_2m&timezone=auto", lat, lon)
json <- jsonlite::fromJSON(url)
temps <- json$hourly$temperature_2m
cat("=== Clima (Open-Meteo) ===\n")
cat("Latitude:", lat, "Longitude:", lon, "\n")
cat("Horas:", length(temps), " | Média:", mean(temps), "°C", " | Desvio:", sd(temps), "\n")
