from datetime import date

def calculate_task_score(task_data):
    """
    Calculates a priority score for a task.
    Higher score = higher priority.
    """
    score = 0
    today = date.today()

    # Parse due_date string to date object
    due = task_data.get("due_date")
    if isinstance(due, str):
        due = date.fromisoformat(due)

    # Urgency: more points for overdue or soon due
    days_until_due = (due - today).days
    if days_until_due < 0:
        score += 120  # Overdue
    elif days_until_due <= 2:
        score += 80
    elif days_until_due <= 7:
        score += 40

    # Importance weighting
    importance = task_data.get("importance", 5)
    score += importance * 5

    # Effort weighting (quick wins)
    hours = task_data.get("estimated_hours", 1)
    if hours <= 1:
        score += 15
    elif hours <= 3:
        score += 5

    # Dependencies (more dependencies = higher score)
    dependencies = task_data.get("dependencies", [])
    score += 10 * len(dependencies)

    return score
