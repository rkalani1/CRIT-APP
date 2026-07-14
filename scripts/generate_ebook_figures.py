import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = r"C:\Users\rkala\CRIT-APP\docs\assets\figures"
os.makedirs(out_dir, exist_ok=True)

# 1. DFR loop (Data, Framework, Results)
def draw_dfr_loop():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.axis('off')
    
    circle1 = plt.Circle((0.3, 0.5), 0.15, color='indigo', alpha=0.6)
    circle2 = plt.Circle((0.7, 0.5), 0.15, color='gold', alpha=0.6)
    circle3 = plt.Circle((0.5, 0.2), 0.15, color='teal', alpha=0.6)
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    
    plt.text(0.3, 0.5, 'Data', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    plt.text(0.7, 0.5, 'Framework', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    plt.text(0.5, 0.2, 'Results', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    
    plt.title("DFR Loop", fontsize=16, fontweight='bold', color='indigo')
    plt.savefig(os.path.join(out_dir, "dfr_loop_new.png"), dpi=300, bbox_inches='tight')
    plt.close()

# 2. Target estimand card
def draw_estimand_card():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')
    
    props = dict(boxstyle='round', facecolor='whitesmoke', alpha=1, edgecolor='indigo', linewidth=2)
    textstr = "\n".join((
        "Target Estimand Framework",
        "-------------------------",
        "1. Population: Who is targeted?",
        "2. Treatment: What is the exact intervention?",
        "3. Intercurrent Events: How are protocol deviations handled?",
        "4. Variable: What is the outcome measure?",
        "5. Population-level Summary: How are we summarizing the effect?"
    ))
    
    ax.text(0.05, 0.5, textstr, transform=ax.transAxes, fontsize=12,
            verticalalignment='center', bbox=props, family='monospace')
            
    plt.title("The Target Estimand", fontsize=16, fontweight='bold', color='indigo')
    plt.savefig(os.path.join(out_dir, "estimand_card_new.png"), dpi=300, bbox_inches='tight')
    plt.close()

# 3. Confounder-mediator
def draw_confounder_mediator():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    
    # Treatment -> Outcome
    ax.annotate("", xy=(0.8, 0.5), xytext=(0.2, 0.5), arrowprops=dict(arrowstyle="->", lw=2, color='black'))
    plt.text(0.1, 0.5, "Treatment", ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))
    plt.text(0.9, 0.5, "Outcome", ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))
    
    # Confounder
    ax.annotate("", xy=(0.2, 0.55), xytext=(0.5, 0.8), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
    ax.annotate("", xy=(0.8, 0.55), xytext=(0.5, 0.8), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
    plt.text(0.5, 0.85, "Confounder", ha='center', va='center', fontsize=12, color='red', bbox=dict(facecolor='white', edgecolor='red'))
    
    # Mediator
    ax.annotate("", xy=(0.5, 0.35), xytext=(0.2, 0.45), arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
    ax.annotate("", xy=(0.8, 0.45), xytext=(0.5, 0.35), arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
    plt.text(0.5, 0.3, "Mediator", ha='center', va='center', fontsize=12, color='blue', bbox=dict(facecolor='white', edgecolor='blue'))
    
    plt.title("Confounding vs Mediation", fontsize=14, fontweight='bold')
    plt.savefig(os.path.join(out_dir, "confounder_mediator_new.png"), dpi=300, bbox_inches='tight')
    plt.close()

# 4. Absolute effects icon array
def draw_icon_array():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    
    for i in range(10):
        for j in range(10):
            color = 'lightgray'
            if i < 2:  # 20% baseline risk
                color = 'salmon'
            if i == 1 and j > 4: # 5% absolute risk reduction
                color = 'green'
            circle = plt.Circle((i*0.1 + 0.05, j*0.1 + 0.05), 0.04, color=color)
            ax.add_patch(circle)
            
    plt.text(0.5, -0.05, "Gray = No event (75)\nRed = Event despite treatment (15)\nGreen = Event prevented by treatment (10)", ha='center', va='top', fontsize=10)
    plt.title("Absolute Effects Icon Array (NNT = 10)", fontsize=14, fontweight='bold')
    plt.savefig(os.path.join(out_dir, "icon_array_new.png"), dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_dfr_loop()
    draw_estimand_card()
    draw_confounder_mediator()
    draw_icon_array()
    print("New original figures generated successfully.")
