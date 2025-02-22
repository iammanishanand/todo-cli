import json
from pathlib import Path
from typing import Optional
import typer

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
DATA_FILE = Path("todo.json")

# Ensure the data file exists
if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")


def read_tasks():
    """Read tasks from the file."""
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return []


def write_tasks(tasks):
    """Write tasks to the file."""
    DATA_FILE.write_text(json.dumps(tasks, indent=4))


@app.command()
def add(task: str):
    """Add a new task to the list."""
    tasks = read_tasks()
    tasks.append({"task": task, "completed": False})
    write_tasks(tasks)
    typer.echo(f"✅ Task added: {task}")


@app.command(name="list")
def list_tasks():
    """List all tasks."""
    tasks = read_tasks()
    if not tasks:
        typer.echo("📭 No tasks found.")
        return

    typer.echo("\n📝 To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        typer.echo(f"{idx}. {task['task']} [{status}]")


@app.command()
def complete(task_number: int = typer.Argument(..., help="Task number to mark as completed")):
    """Mark a task as completed."""
    tasks = read_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        write_tasks(tasks)
        typer.echo(f"🎯 Task {task_number} marked as completed.")
    else:
        typer.echo("⚠️ Invalid task number.")


@app.command()
def delete(task_number: int = typer.Argument(..., help="Task number to delete")):
    """Delete a task from the list."""
    tasks = read_tasks()
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        write_tasks(tasks)
        typer.echo(f"🗑️ Task deleted: {deleted_task['task']}")
    else:
        typer.echo("⚠️ Invalid task number.")


if __name__ == "__main__":
    app()
