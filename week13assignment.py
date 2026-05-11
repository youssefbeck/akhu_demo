def streaming_report(input_path, output_path, engagement_threshold):
    """Processes streaming log data, writes a report, and returns a summary dict."""
    records = [] 
    with open(input_path, "r") as fin:
        for line in fin:
            if not line.strip(): continue # Skip empty lines
            user, raw_vals = line.strip().split("|") # Split record
            vals = [float(v.strip()) for v in raw_vals.split(",")] # Convert values
            avg = round(sum(vals) / len(vals), 1) # Calculate average
            records.append({"name": user, "avg": avg, "peak": max(vals), "low": min(vals)})
    total_users = len(records) # Aggregate counts
    platform_avg = round(sum(r["avg"] for r in records) / total_users, 1) # Global average
    records.sort(key=lambda x: x["avg"], reverse=True) # Sort descending
    top = f"{records[0]['name']} ({records[0]['avg']} min)" # Top performer
    bottom = f"{records[-1]['name']} ({records[-1]['avg']} min)" # Bottom performer
    thresh = float(engagement_threshold) # Convert threshold
    active = [r for r in records if r["avg"] >= thresh] # Filter active
    with open(output_path, "w") as fout: # Write report
        fout.write("Streaming Engagement Report\n")
        fout.write("==============================\n")
        for r in records:
            fout.write(f"{r['name']}: avg={r['avg']}min peak={r['peak']}min low={r['low']}min\n")
        fout.write(f"\nPlatform Average:  {platform_avg} min\n")
        fout.write(f"Most Engaged:      {top}\n")
        fout.write(f"Least Engaged:     {bottom}\n")
        fout.write(f"Active ({int(thresh)}min+): {len(active)}/{total_users}\n")
    return { # Return summary
        "users": total_users,
        "platform_avg": platform_avg,
        "most_engaged": top,
        "least_engaged": bottom,
        "active_count": len(active)
    }
if __name__ == "__main__":
    with open("streaming.txt", "w") as f:
        f.write("Alice|95,110,88,102\nBob|22,18,25,20\nCarol|145,160,138,152\nDave|68,72,65,70\nEve|35,40,30,38")
    
    with open("streaming2.txt", "w") as f:
        f.write("Sam|125,130,120\nJordan|30,28,35")
    print("Running Example 1...")
    res1 = streaming_report("streaming.txt", "streaming_report.txt", "60")
    print(res1)

    print("\nRunning Example 2...")
    res2 = streaming_report("streaming2.txt", "streaming_report2.txt", "60")
    print(res2)