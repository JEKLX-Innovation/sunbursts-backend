import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
from .models import SunburstElement
from django.shortcuts import render, get_object_or_404, redirect

def create_df():
    sunburst_elements = SunburstElement.objects.all()
    # project = get_object_or_404(SunburstElement.objects.prefetch_related('projects'), pk=pk)
    # context = {'project': project}
    print("Survey Responses:", sunburst_elements)
    data = []
    for sunburst_element in sunburst_elements:
        data.append({
            'Element': sunburst_element.element_name,
            'Point Score': sunburst_element.point_score,
            'Need Score': sunburst_element.need_score,
            'Score': sunburst_element.score,
            'Category': sunburst_element.category,
        })
    df_data = pd.DataFrame(data)
    # print("df", df_data)
    return df_data
    # return render(request, context)


def generate_graph():
    df = create_df()
    # Read data from CSV file
    # df = pd.read_csv('StakeholderInputAnalysis.xlsx - Mock Data.csv')

    # Sort and process the dataset
    df_sorted = (
        df.groupby(["Category"])
        .apply(lambda x: x.sort_values(["Score"], ascending=True))
        .reset_index(drop=True)
    )

    # Adjusting values, labels, and groups for the dataset
    VALUES = df_sorted["Score"].values
    LABELS = df_sorted["Element"].values
    GROUP = df_sorted["Category"].values
    print(GROUP)

    # Calculation of angles and indexing needs to be adjusted for the data structure
    PAD = 3  # Keeping the padding the same for consistency
    ANGLES_N = len(VALUES) + PAD * len(np.unique(GROUP))
    ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
    WIDTH = (2 * np.pi) / len(ANGLES)
    GROUPS_SIZE = [len(i[1]) for i in df_sorted.groupby("Category")]
    offset = 0
    IDXS = []
    for size in GROUPS_SIZE:
        IDXS += list(range(offset + PAD, offset + size + PAD))
        offset += size + PAD

    # Colors for point score and need score within each category
    point_score_colors = ["#6699CC", "#FFCC66", "#99CC99", "#CC99CC"]
    need_score_colors = ["#336699", "#FF9933", "#669966", "#996699"]

    # Create figure and axis using the Agg backend
    plt.switch_backend('Agg')
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw={"projection": "polar"})
    ax.set_theta_offset(np.pi / 2)
    ax.set_ylim(-220, 420)  # Adjusting ylim to accommodate category labels below
    ax.set_frame_on(False)
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # Plotting bars for point score and need score separately
    for idx, (angle, value, point_score, need_score, category) in enumerate(zip(ANGLES[IDXS], VALUES, df_sorted["Point Score"], df_sorted["Need Score"], df_sorted["Category"])):
        category_idx = ["E", "BR", "W", "S"].index(category)
        # Bar for point score
        ax.bar(angle, point_score, width=WIDTH, color=point_score_colors[category_idx], edgecolor="white", linewidth=2)
        # Bar for need score, stacked on top of point score
        ax.bar(angle, need_score, width=WIDTH, color=need_score_colors[category_idx], edgecolor="white", linewidth=2, bottom=point_score)

    # Helper function for label rotation and alignment
    def get_label_rotation(angle, offset):
        rotation = np.rad2deg(angle + offset)
        if angle <= np.pi:
            alignment = "right"
            rotation = rotation + 180
        else:
            alignment = "left"
        return rotation, alignment

    # Function to add labels to the plot
    def add_labels(angles, values, labels, offset, ax):
        padding = 4
        for angle, value, label in zip(angles, values, labels):
            rotation, alignment = get_label_rotation(angle, offset)
            ax.text(
                x=angle,
                y=value + padding,
                s=label,
                ha=alignment,
                va="center",
                rotation=rotation,
                rotation_mode="anchor"
            )

    add_labels(ANGLES[IDXS], VALUES, LABELS, np.pi / 2, ax)

    # Adjusting text and reference lines as before
    offset = 0
    for group, size in zip(["BR", "E", "S", "W"], GROUPS_SIZE):
        start_angle = ANGLES[offset + PAD]
        end_angle = ANGLES[offset + size + PAD - 1]
        num_bars = len(np.unique(df_sorted["Element"]))
        x1 = np.linspace(start_angle, end_angle, num=num_bars)
        
        ax.plot(x1, [-1] * num_bars, color="#333333")

        ax.text(np.mean(x1), -30, group, color="#333333", fontsize=14, fontweight="bold", ha="center", va="center")
        x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=50)
        for ref_val in range(50, 201, 50):
            ax.plot(x2, [ref_val] * 50, color="#BEBEBE", lw=0.8)
            ax.text(x2[0], ref_val, str(ref_val), color="#333333", fontsize=10, ha="right", va="center")
        offset += size + PAD

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)
    
    return buffer
