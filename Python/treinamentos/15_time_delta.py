from datetime import datetime, timedelta

hoje = datetime.now()

futuro = hoje + timedelta(days=10)

print("Hoje:", hoje)
print("Daqui 10 dias:", futuro)

