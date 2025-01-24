def clear_window(root):
    """Clear all widgets from the root window."""
    for widget in root.winfo_children():
        widget.destroy()
