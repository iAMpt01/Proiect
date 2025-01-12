import requests
from rich.console import Console
from rich.table import Table

API_URL = "http://127.0.0.1:8000"
console = Console()

# Citește datele unui pacient
def get_patient_data():
    response = requests.get(f"{API_URL}/data")
    if response.status_code == 200:
        data = response.json()
        table = Table(title="Date Pacienți")
        table.add_column("ID Pacient", style="cyan", justify="center")
        table.add_column("Ritmul Cardiac", style="magenta", justify="center")
        table.add_column("Temperatura", style="yellow", justify="center")
        table.add_column("Tensiunea", style="green", justify="center")
        table.add_column("Timestamp", style="white", justify="center")

        for entry in data:
            table.add_row(
                str(entry["patient_id"]),
                str(entry["heart_rate"]),
                f'{entry["temperature"]:.1f}',
                entry["blood_pressure"],
                entry["timestamp"]
            )
        console.print(table)
    else:
        console.print("[bold red]Eroare la citirea datelor.[/bold red]")

# Simulează citirea de la senzor
def simulate_sensor_data(patient_id: int):
    response = requests.get(f"{API_URL}/sensor/{patient_id}/data")
    if response.status_code == 200:
        data = response.json()
        console.print(f"[bold green]Datele pacientului cu ID {patient_id}:[/bold green]")
        console.print(data)
    else:
        console.print("[bold red]Eroare la simularea datelor.[/bold red]")

# Exemplu de utilizare
if __name__ == "__main__":
    console.print("[bold cyan]Simulăm datele pentru pacientul 1...[/bold cyan]")
    simulate_sensor_data(1)
    console.print("[bold cyan]Citim toate datele pacienților...[/bold cyan]")
    get_patient_data()
