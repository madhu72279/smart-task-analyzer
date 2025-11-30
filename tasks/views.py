from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        tasks = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Add score for each task
    for task in tasks:
        task['score'] = calculate_task_score(task)

    # Sort tasks by score descending
    tasks.sort(key=lambda x: x['score'], reverse=True)
    return JsonResponse(tasks, safe=False)
